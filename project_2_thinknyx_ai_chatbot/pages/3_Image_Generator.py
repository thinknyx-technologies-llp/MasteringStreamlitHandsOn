import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image Generator", page_icon="🎨", layout="wide")
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")
st.title("🎨 AI Image Generator")
st.caption("Generate stunning images using Google's Imagen model via the GenAI SDK.")

if "image_model" not in st.session_state:
    st.session_state.image_model = "gemini-2.5-flash-image"

api_key = st.secrets.get("GOOGLE_API_KEY")
if "api_key" in st.session_state and st.session_state.api_key:
    api_key = st.session_state.api_key

if not api_key or api_key == "YOUR_GOOGLE_API_KEY_HERE":
    st.warning("Please configure your Google API Key in the Settings page.")
    st.stop()

client = genai.Client(api_key=api_key)

with st.form("image_gen_form"):
    prompt = st.text_input("Enter your prompt:", placeholder="A futuristic city at sunset in cyberpunk style...")
    aspect_ratio = st.selectbox("Aspect Ratio", ["1:1", "16:9", "4:3", "3:4", "9:16"])
    submit_btn = st.form_submit_button("Generate Image 🪄")

if submit_btn and prompt:
    with st.spinner("Generating image... This might take a few seconds."):
        try:
            # Map aspect ratio to SDK types if necessary, or just use default.
            # For simplicity, using default configuration.
            result = client.models.generate_images(
                model=st.session_state.image_model,
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    output_mime_type="image/jpeg",
                    aspect_ratio=aspect_ratio
                )
            )
            
            for generated_image in result.generated_images:
                image = Image.open(BytesIO(generated_image.image.image_bytes))
                st.image(image, caption=f"Prompt: {prompt}", use_container_width=True)
                
                # Option to download
                buf = BytesIO()
                image.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download Image",
                    data=byte_im,
                    file_name="generated_image.jpg",
                    mime="image/jpeg"
                )
        except Exception as e:
            st.error(f"Failed to generate image. Error: {e}")
