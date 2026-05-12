import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import re
from google import genai

st.set_page_config(page_title="File Q&A", page_icon="📄", layout="wide")
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")
st.title("📄 Ask Questions to Your File")
st.caption("Upload a dataset (CSV/Excel) or a Text file, chat with it, and even generate charts dynamically!")

if "vision_model" not in st.session_state:
    st.session_state.vision_model = "gemini-2.5-flash"

api_key = st.secrets.get("GOOGLE_API_KEY")
if "api_key" in st.session_state and st.session_state.api_key:
    api_key = st.session_state.api_key

if not api_key or api_key == "YOUR_GOOGLE_API_KEY_HERE":
    st.warning("Please configure your Google API Key in the Settings page.")
    st.stop()

client = genai.Client(api_key=api_key)

uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "txt", "md"])

if "file_messages" not in st.session_state:
    st.session_state.file_messages = []

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    
    # Process Data
    df = None
    file_content = ""
    
    if file_type in ['csv', 'xlsx']:
        try:
            if file_type == 'csv':
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.write("### Data Preview")
            st.dataframe(df.head())
            # Clean column names to prevent KeyError
            df.columns = df.columns.str.strip()
            file_content = f"The user uploaded a dataset with columns: {', '.join(df.columns.tolist())}. Here is the first 5 rows of data:\n{df.head().to_string()}"
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        file_content = uploaded_file.getvalue().decode("utf-8")
        st.write("### File Content Preview")
        st.text(file_content[:1000] + ("..." if len(file_content) > 1000 else ""))

    # Display chat history specific to this file session
    for message in st.session_state.file_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question or request a chart (e.g., 'Plot a bar chart of X vs Y')"):
        st.chat_message("user").markdown(prompt)
        st.session_state.file_messages.append({"role": "user", "content": prompt})
        
        system_instructions = f"""You are an AI data assistant. 
Context data: 
{file_content}

If the user asks a question, answer it based on the data.
If the user asks to draw or plot a chart based on the dataframe, generate strictly Python Streamlit code using `st.plotly_chart` or `st.bar_chart` etc.
Assume the pandas dataframe is already loaded as a variable named `df`.
IMPORTANT: Always use the exact column names as provided in the context data. Do not hallucinate or guess column names.
Wrap your Python code in ```python ... ``` block. Do not use st.write for normal text, only return python code for charting.
"""
        
        contents = [{'role': 'user', 'parts': [{'text': system_instructions + "\n\nUser Question: " + prompt}]}]
        
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                try:
                    response = client.models.generate_content_stream(
                        model=st.session_state.vision_model,
                        contents=contents
                    )
                    
                    def stream_data(response):
                        for chunk in response:
                            if chunk.text:
                                yield chunk.text

                    reply = st.write_stream(stream_data(response))
                    st.session_state.file_messages.append({"role": "assistant", "content": reply})
                    
                    # Check if the response contains python code block to execute
                    if "```python" in reply and df is not None:
                        code_blocks = re.findall(r'```python(.*?)```', reply, re.DOTALL)
                        for code in code_blocks:
                            st.info("Executing generated chart code...")
                            try:
                                # Provide safe local environment
                                local_env = {"df": df, "st": st, "pd": pd, "plt": plt, "px": px}
                                exec(code.strip(), globals(), local_env)
                            except Exception as exec_err:
                                st.error(f"Error executing chart code: {exec_err}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
