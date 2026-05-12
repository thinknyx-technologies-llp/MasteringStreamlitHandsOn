import streamlit as st

# Text Elements

st.title("Hello Thinknyx")

st.header("This is a header")

st.subheader("This is Subheader")

st.write("Hello from Thinknyx Team")

st.markdown("*Thinknyx* is really **cool**")

'''
# This is a markdown content.

_Italic_
- List Item

'''

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

'---'

# Data elements

import pandas as pd

# Create a simple DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

st.write(df)

st.table(df)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.json(
    {
        "Team": "Thinknyx",
        "Members": [
            "Yogesh Raheja",
            "Madhuri Jha",
            "Aryan Kothiyal",
            "Dheeraj Sain"
        ]
    },
    expanded=2,
)

st.audio("https://woolyss.com/f/audio-sample.mp3")

st.video("https://cdn.pixabay.com/video/2016/12/31/6962-197634410_large.mp4")

st.image("https://tsa.thinknyx.com/assets/images/udemy/ai.png", 
         caption="AI Ecosystem for the Absolute Beginners")

st.logo("https://www.thinknyx.com/wp-content/uploads/2022/05/logo_thinknyx.png", 
        size="large", link=None, icon_image=None)