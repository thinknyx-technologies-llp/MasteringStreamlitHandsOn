import streamlit as st
import os
from utils.data_loader import list_datasets

st.set_page_config(
    page_title="AI Adoption Analytics App",
    layout="wide",
    page_icon="🚀"
)

st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

st.title("📊 AI Adoption Analytics & Data Explorer")

st.markdown("""
Welcome to the AI Adoption Analytics App. This dashboard provides deep insights into AI adoption trends across different regions and industries.
""")

# File Upload Section
st.header("📂 Upload New Dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


if uploaded_file is not None:
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    file_path = os.path.join(data_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Successfully uploaded: {uploaded_file.name}")


# Current Datasets
st.subheader("📋 Available Datasets")
datasets = list_datasets()
if datasets:
    for ds in datasets:
        st.write(f"- {ds}")
else:
    st.write("No datasets available. Please upload one.")

st.divider()

