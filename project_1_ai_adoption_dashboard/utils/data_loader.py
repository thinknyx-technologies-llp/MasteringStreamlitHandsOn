import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data(file_path="data/ai_india_data.csv"):
    return pd.read_csv(file_path)

def list_datasets():
    data_dir = "data"
    if not os.path.exists(data_dir):
        return []
    return [f for f in os.listdir(data_dir) if f.endswith(".csv")]