import streamlit as st

st.header("The Counter Dilemma")

st.subheader("Without Session State (The Forgetful Counter)")

if "normal_counter" not in locals():
    normal_counter = 0

if st.button("Increment Normal Counter"):
    normal_counter += 1
    
st.write(f"Normal Counter is at: **{normal_counter}**")

st.divider()

st.subheader("With Session State (The Smart Counter)")
# We initialize the variable inside Streamlit's session_state dictionary
if "smart_counter" not in st.session_state:
    st.session_state.smart_counter = 0

if st.button("Increment Smart Counter"):
    st.session_state.smart_counter += 1

st.write(f"Smart Counter is at: **{st.session_state.smart_counter}**")