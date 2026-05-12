import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="wide")
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")
st.title("💬 AI Chatbot")
st.caption("A conversational interface powered by Google Gemini.")

# Ensure models are in session state
if "chat_model" not in st.session_state:
    st.session_state.chat_model = "gemini-2.5-flash"

# Get API key from secrets or session state
api_key = st.secrets.get("GOOGLE_API_KEY")
if "api_key" in st.session_state and st.session_state.api_key:
    api_key = st.session_state.api_key

if not api_key or api_key == "YOUR_GOOGLE_API_KEY_HERE":
    st.warning("Please configure your Google API Key in the Settings page or `.streamlit/secrets.toml`.")
    st.stop()

# Initialize Client
client = genai.Client(api_key=api_key)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Prepare contents for the model
    # Convert history into a format the GenAI SDK expects
    contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append({'role': role, 'parts': [{'text': msg["content"]}]})
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content_stream(
                    model=st.session_state.chat_model,
                    contents=contents
                )
                
                def stream_data(response):
                    for chunk in response:
                        if chunk.text:
                            yield chunk.text

                full_response = st.write_stream(stream_data(response))
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
