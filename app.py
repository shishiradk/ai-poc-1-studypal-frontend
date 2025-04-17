import streamlit as st
import requests

st.set_page_config(
    page_title="StudyPal",
    page_icon="🤖",
    layout="centered" #wide
)

st.title("🤖 StudyPal Application")

api_url = "http://127.0.0.1:8000/ask"

#get user input
user_question = st.text_input(label="Ask your question",placeholder="eg. that is ML?")

#button to trigger the API
if st.button("get Answer"):



    response= requests.post(
        url = api_url,
        json = {"question": user_question}
    )

    result = response.json()
    answer = result["answer"]

    st.success(answer)



