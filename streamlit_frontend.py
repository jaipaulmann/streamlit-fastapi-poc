import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# taking user inputs
selection = st.selectbox('What operation do you want to perform?',
                         ('Addition','Subtraction','Multiplication','Division'))
st.write("")
st.write("Select the numbers from slider below")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

# converting inputs into a json format
inputs = {"operation":selection, "x":x, "y":y}

# when the user clicks on button it will fetch the API
if st.button('Calculate'):
    response = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(inputs))

    st.subheader(f"Response from API = {response.text}")

# to test app, run from same directory as streamlit.py file: streamlit run streamlit_frontend.py
# or without activating the virtual env: ??