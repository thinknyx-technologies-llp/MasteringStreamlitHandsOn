import streamlit as st

st.title("Thinknyx Experience Form")

# Create a form container

with st.form(key="exp_form"):
    st.write("Please fill out the details below:")

    name = st.text_input("Name")
    total_exp = st.number_input("Experience", min_value=0, max_value=40)

    department = st.selectbox("Department", 
                              ["Engineering", "Marketing", "Sales", "HR"])

    submit_button = st.form_submit_button(label="Submit")

# st.write(name, total_exp, department)

if submit_button:
    print("---------New Form Submission---------")
    print(f"Name: {name}")
    print(f"Experience: {total_exp}")
    print(f"Department: {department}")
    print("------------------")

    st.success(f"Thanks {name}! Your data is stored.")

