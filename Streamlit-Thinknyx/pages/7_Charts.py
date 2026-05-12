import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

'# Charts'


df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["nyx", "rook", "tsa"])

'### Line Chart'
st.line_chart(df)


'### Bar Chart'
st.bar_chart(df)

'---'

'### Area Chart'

st.area_chart(df,  color=["#FF000080", "#0000FF80", "#AAF003"])


'---'

'### Scatter Chart'
st.scatter_chart(df, color=["#FF000080", "#0000FF80", "#AAF003"])