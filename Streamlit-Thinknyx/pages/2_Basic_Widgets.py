import streamlit as st

pri = st.button("Thinknyx", type="primary")

sec = st.button("Thinknyx", type="secondary")

if pri:
    st.balloons()
elif sec:
    st.write("It's Secondory")
else:
    st.write("Press any Button")


agree = st.checkbox("I agree")

if agree:
    st.write("Thankyou from Thinknyx")


import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)


title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)