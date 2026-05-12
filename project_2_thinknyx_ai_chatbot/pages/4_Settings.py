import streamlit as st
import os

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")
st.title("⚙️ Settings & Configuration")
st.caption("Manage your API keys and select models for each tool.")

# Models list
CHAT_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash-exp", "gemini-1.5-pro"]
VISION_MODELS = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-1.5-pro", "gemini-1.5-flash"]
IMAGE_MODELS = ["gemini-2.5-flash-image"]

# Init defaults
if "chat_model" not in st.session_state:
    st.session_state.chat_model = CHAT_MODELS[0]
if "vision_model" not in st.session_state:
    st.session_state.vision_model = VISION_MODELS[0]
if "image_model" not in st.session_state:
    st.session_state.image_model = IMAGE_MODELS[0]
if "api_key" not in st.session_state:
    st.session_state.api_key = st.secrets.get("GOOGLE_API_KEY", "")

st.header("🔑 API Configuration")
api_key_input = st.text_input(
    "Google Gemini API Key", 
    value=st.session_state.api_key, 
    type="password",
    help="Enter your Google Gemini API key. This will override the secrets.toml file for this session."
)

if st.button("Save API Key"):
    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("API Key saved securely in session state!")
    else:
        st.error("Please enter a valid API key.")

st.divider()

st.header("🧠 Model Selection")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💬 Chatbot Model")
    chat_idx = CHAT_MODELS.index(st.session_state.chat_model) if st.session_state.chat_model in CHAT_MODELS else 0
    new_chat_model = st.selectbox("Select Model", CHAT_MODELS, index=chat_idx, key="chat_sel")

with col2:
    st.subheader("📄 File Q&A Model")
    vis_idx = VISION_MODELS.index(st.session_state.vision_model) if st.session_state.vision_model in VISION_MODELS else 0
    new_vis_model = st.selectbox("Select Model", VISION_MODELS, index=vis_idx, key="vis_sel")

with col3:
    st.subheader("🎨 Image Model")
    img_idx = IMAGE_MODELS.index(st.session_state.image_model) if st.session_state.image_model in IMAGE_MODELS else 0
    new_img_model = st.selectbox("Select Model", IMAGE_MODELS, index=img_idx, key="img_sel")

if st.button("Update Models"):
    st.session_state.chat_model = new_chat_model
    st.session_state.vision_model = new_vis_model
    st.session_state.image_model = new_img_model
    st.success("Model preferences updated successfully!")

st.divider()
st.info("""
### Tips:
- To make API key persistent across restarts, edit `.streamlit/secrets.toml` directly.
- The `gemini-2.5-flash` model is recommended for standard tasks due to speed and efficiency.
- `gemini-2.5-flash-image` offers high-quality image generation.
""")
