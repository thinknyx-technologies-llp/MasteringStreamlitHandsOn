import streamlit as st

'## Enhancing UI'

st.set_page_config(
    page_title="ThinkRook",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

tab1, tab2 = st.tabs(["Course 1", "Course 2"])

with tab1:
    st.header("This is Coure 1")
    st.image("https://tsa.thinknyx.com/assets/images/udemy/kubernetes.png", width=600)

with tab2:
    st.header("This is Course 2")
    st.image("https://tsa.thinknyx.com/assets/images/udemy/git.jpg", width=600)


import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(df)

tab2.subheader("A tab with the data")
tab2.write(df)


'---'
