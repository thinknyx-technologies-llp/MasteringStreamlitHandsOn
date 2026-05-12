import streamlit as st
from utils.data_loader import load_data, list_datasets
import os

st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

# Dataset Selection in Sidebar
datasets = list_datasets()
selected_dataset = st.sidebar.selectbox("Select Dataset", datasets, index=0 if datasets else None)

if not selected_dataset:
    st.title("💼 Professional & Salary Distribution")
    st.warning("No datasets found. Please upload one in the Home page.")
    st.stop()

file_path = os.path.join("data", selected_dataset)
df = load_data(file_path)

st.title(f"💼 Workforce Insights: {selected_dataset}")
st.markdown("Explore how geography and job titles influence compensation and career progression.")


# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Workspace")
city_filter = st.sidebar.multiselect("Select Cities", df["city"].unique(), default=df["city"].unique())
role_filter = st.sidebar.multiselect("Select Roles", df["role"].unique(), default=df["role"].unique())

filtered_df = df[
    (df["city"].isin(city_filter)) &
    (df["role"].isin(role_filter))
]

# --- Row 1: Salary vs Experience ---
st.subheader("📈 The Salary Growth Path")

# Preparing data: Average salary per year of experience to make the line smooth
trend_df = filtered_df.groupby(["experience_years", "role"])["salary_lpa"].mean().reset_index()

# Using a line chart for a clearer "path" of growth
st.line_chart(
    trend_df,
    x="experience_years",
    y="salary_lpa",
    color="role",
)

st.info("""
**How to read this:** This line chart shows the 'career trajectory.' Each line represents a different role. 
The steeper the line, the faster the salary increases as you gain experience. 
It’s easier to see here which roles 'peak' early and which ones have long-term growth.
""")

# --- Row 2: Distribution and Pay ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Role Distribution")
    # Horizontal bar for better label reading
    role_dist = filtered_df["role"].value_counts().sort_values(ascending=True)
    st.bar_chart(role_dist, color="#673ab7")
    
    st.caption("**Insight:** This shows the workforce density for the selected filters. A high concentration of 'Data Scientists' or 'AI Engineers' usually indicates a tech-heavy hub.")

with col2:
    st.subheader("Average Salary by Role")
    # Grouping and sorting
    salary_role = filtered_df.groupby("role")["salary_lpa"].mean().sort_values(ascending=False)
    st.bar_chart(salary_role, color="#f44336")
    
    st.caption("**Insight:** Comparison of median pay scales. Roles specializing in specific AI infrastructure often command a premium over general analyst positions.")

# --- Summary Metric Footnote ---
if not filtered_df.empty:
    top_role = salary_role.idxmax()
    st.success(f"💡 In your current selection, **{top_role}** is the highest paying role on average.")