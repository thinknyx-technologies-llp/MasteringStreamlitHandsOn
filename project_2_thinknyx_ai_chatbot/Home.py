import streamlit as st

st.set_page_config(
    page_title="Thinknyx AI Hub",
    page_icon="🤖",
    layout="wide"
)

st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

st.title("🤖 Thinknyx AI Hub")
st.markdown("""
Welcome to the **Thinknyx AI Hub**! This multipage Streamlit application demonstrates the power of Google's Gemini Models using the new Google GenAI SDK.

### 👈 Navigate from the sidebar to explore:
- **💬 Chatbot**: A conversational AI with memory and session state.
- **📄 File Q&A**: Upload documents or data files, ask questions, and even generate charts dynamically!
- **🎨 Image Generator**: Turn your textual prompts into stunning images.
- **⚙️ Settings**: Configure your API key and choose the Gemini models for different tasks.

#### Setup Instructions:
1. Go to the **Settings** page to verify or enter your Google API Key.
2. Ensure you have your `GOOGLE_API_KEY` set in `.streamlit/secrets.toml`.

Let's explore the power of GenAI! 🚀
""")

# Initialize session state for models if not exist
if "chat_model" not in st.session_state:
    st.session_state.chat_model = "gemini-2.5-flash"
if "vision_model" not in st.session_state:
    st.session_state.vision_model = "gemini-2.5-flash"
if "image_model" not in st.session_state:
    st.session_state.image_model = "gemini-2.5-flash-image"
