import streamlit as st
from utils.data_loader import load_data, list_datasets

import os

st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

# Dataset Selection in Sidebar
datasets = list_datasets()
selected_dataset = st.sidebar.selectbox("Select Dataset", datasets, index=0 if datasets else None)

if selected_dataset:
    file_path = os.path.join("data", selected_dataset)
    df = load_data(file_path)
    st.title(f"📊 AI Adoption Overview: {selected_dataset}")
else:
    st.title("AI Adoption Overview")
    st.warning("No datasets found. Please upload one in the Home page.")
    st.stop()


# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Records", df.shape[0])
col2.metric("AI Adoption Rate", f"{df['ai_adopted'].mean()*100:.1f}%")
col3.metric("Avg Salary", f"{df['salary_lpa'].mean():.1f} LPA")

# City-wise AI Adoption
st.subheader("AI Adoption by City")
city_adoption = df.groupby("city")["ai_adopted"].mean()
st.bar_chart(city_adoption)

# Industry-wise Adoption
st.subheader("AI Adoption by Industry")
industry_adoption = df.groupby("industry")["ai_adopted"].mean()
st.bar_chart(industry_adoption)