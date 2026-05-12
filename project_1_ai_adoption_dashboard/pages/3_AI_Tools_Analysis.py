import streamlit as st
from utils.data_loader import load_data, list_datasets
import os

st.set_page_config(page_title="AI Market Analysis", layout="wide")
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

# Dataset Selection in Sidebar
datasets = list_datasets()
selected_dataset = st.sidebar.selectbox("Select Dataset", datasets, index=0 if datasets else None)

if not selected_dataset:
    st.title("📊 AI Tooling & Salary Insights")
    st.warning("No datasets found. Please upload one in the Home page.")
    st.stop()

file_path = os.path.join("data", selected_dataset)
df = load_data(file_path)

st.title(f"📊 AI Tooling Insights: {selected_dataset}")


st.markdown("This dashboard provides a snapshot of how different AI tools impact compensation and adoption across industries.")

# --- Row 1: Usage and Salary ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Most Used AI Tools")
    tool_usage = df["primary_ai_tool"].value_counts().sort_values(ascending=False)
    st.bar_chart(tool_usage, color="#2979ff")
    
    st.info("**Insight:** TensorFlow and PyTorch remain the dominant frameworks in this dataset, showing a strong preference for deep learning tools in professional roles.")

with col2:
    st.subheader("Avg Salary by Tool (LPA)")
    tool_salary = df.groupby("primary_ai_tool")["salary_lpa"].mean().sort_values(ascending=False)
    st.bar_chart(tool_salary, color="#ff9100")
    
    st.info("**Insight:** Cloud-based AI tools (Azure & AWS) are associated with higher average salaries, likely due to their use in enterprise-level architecture.")

st.divider()

# --- Row 2: Adoption Rate ---
st.subheader("AI Adoption Rate by Primary Tool")
# Calculate mean adoption (0 to 1)
tool_adoption = df.groupby("primary_ai_tool")["ai_adopted"].mean().sort_values(ascending=False)

# Display chart
st.bar_chart(tool_adoption, color="#00e676")

# Detailed description
st.markdown("""
**About this Graph:**
This chart represents the percentage of projects where AI has been fully adopted based on the primary tool used. 
* A value of **1.0** means 100% adoption.
* Tools like **ChatGPT** and **Azure AI** show high adoption rates, suggesting they are being moved into production faster than experimental frameworks.
""")

st.divider()

# --- Row 3: Raw Data for reference ---
with st.expander("📂 View Detailed Dataset"):
    st.write("Below is the filtered raw data used to generate the insights above.")
    st.dataframe(df, use_container_width=True)