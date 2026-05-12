import streamlit as st

st.title("ThinkRook")

# Page config
st.set_page_config(page_title="ThinkRook", layout="wide")

# ------------------ LOGO ------------------
st.logo("https://dme2wmiz2suov.cloudfront.net/Institution(8663)/Logo/4216689-ThinkRook_Logo.png", size="large")

# ------------------ SIDEBAR ------------------
st.sidebar.title("📚 ThinkRook")
page = st.sidebar.radio("Navigate", ["Home", "Courses"])

st.write(f"Smart Counter is at: **{st.session_state.smart_counter}**")

if page == "Home":
    st.title("Transform Your Future")
    st.subheader("Master In-Demand Skills with Interactive Learning")

    st.write("""
    Learn Cloud, DevOps, and AI with hands-on projects.
    Build real-world skills and grow your career.
    """)

    if st.button("Start Learning"):
        st.success("Go to Courses section from the sidebar")

    st.divider()

    st.subheader("Popular Domains")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Cloud", "AWS, Azure")
    with col2:
        st.metric("DevOps", "CI/CD, Docker")
    with col3:
        st.metric("AI", "ML, GenAI")

elif page == "Courses":
    st.title("Explore Courses")

    courses = {
        "Cloud Computing": ["AWS Basics", "Azure Fundamentals"],
        "DevOps": ["Docker Mastery", "Kubernetes Guide"],
        "AI": ["Intro to ML", "GenAI with Python"]
    }

    category = st.selectbox("Select Category", list(courses.keys()))

    st.subheader(f"{category} Courses")

    for course in courses[category]:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(course)
        with col2:
            if st.button("Enroll", key=course):
                st.success(f"Enrolled in {course}")
