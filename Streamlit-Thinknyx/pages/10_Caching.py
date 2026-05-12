import streamlit as st
import time
import pandas as pd

st.header("Caching")

st.subheader("The Problem: The 'Laggy' App")


def fetch_data_slowly():
    time.sleep(3)
    return pd.DataFrame({"Category": ["A", "B", "C"], "Values": [10, 20, 30]})

st.write("Loading raw data without caching...")
start_time_slow = time.time()

with st.spinner("Fetching data slowly..."):
    df_slow = fetch_data_slowly()
    
end_time_slow = time.time()

st.error(f"Load time: **{end_time_slow - start_time_slow:.2f} seconds**")
st.dataframe(df_slow)


st.slider("Interact with me (I cause the app to freeze!)", 1, 10, 1, key="slider1")

st.divider()


st.subheader("The Solution: @st.cache_data")

# The exact same function, but WITH the caching decorator
@st.cache_data
def fetch_data_fast():
    time.sleep(3) # Simulating the same 3-second delay
    return pd.DataFrame({"Category": ["X", "Y", "Z"], "Values": [100, 200, 300]})

st.write("Loading data WITH caching...")
start_time_fast = time.time()

with st.spinner("Fetching data fast..."):
    df_fast = fetch_data_fast()
    
end_time_fast = time.time()

st.success(f"Load time: **{end_time_fast - start_time_fast:.2f} seconds**")
st.dataframe(df_fast)

st.slider("Interact with me now!", 1, 10, 1, key="slider2")

st.divider()

st.subheader("Databases and ML Models (@st.cache_resource)")

# Used for global objects that aren't just raw data
@st.cache_resource
def setup_database_connection():
    time.sleep(2) # Simulating a slow connection handshake
    return "Database Connection Established! 🟢"
    
conn = setup_database_connection()
st.info(conn)