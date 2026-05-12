import streamlit as st

# st.write("DB username:", st.secrets["db_username"])
# st.write("DB password:", st.secrets["db_password"])

# st.write("API KEY:", st.secrets["API_KEY"])

api_key = st.secrets["API_KEY"]

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents="What is Streamlit? Explain it to me in 20 words."
)

st.write(response.text)