import streamlit as st

age  = st.slider("Select you age")

st.write(age)

select = st.selectbox("Select contact mode",
                      ["Email", "Phone", "Message"]
                      )
st.write(select)

st.multiselect("what are your platforms for learning new technologies",
               ["Thinknyx", "ThinkRook", "TSA", "Thinknyx YouTube"]
               )

'---'

import pandas as pd
import streamlit as st

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)


import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)


'---'

# Form

import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")