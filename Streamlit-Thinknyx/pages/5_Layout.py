import streamlit as st

'## Layouts & Styling'

col1, col2, col3 = st.columns(3, border=True)

col1.write("Thinknyx " * 10)
col2.write("ThinkRook " * 5)
col3.subheader("Thinknyx & ThinkRook")

'---'

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")

'---'

with st.expander("About"):
    st.write("Thinknyx Technologies is a Cloud Native company, specialized in designing "
    "and implementing IT Automation/DevOps/Containerization solutions. ")

'---'

with st.sidebar:
    st.header("Thinknyx")
    st.markdown('---')

    # st.button("Login", type="primary")
    # st.button("SignUp", type="secondary")

    add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Phone", "SMS"))

    col1, col2 = st.columns(2)

    col1.button("Login", type="primary")
    col2.button("SignUp", type="secondary")