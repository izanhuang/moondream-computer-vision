import streamlit as st

from constants import page_constants
from helper import upload_image

def question_page(moondream):
    st.title(page_constants["question"]["title"])
    st.write(page_constants["question"]["subtitle"])
    image = upload_image(page_constants["question"]["title"])

    if image:
        question = st.text_input("What would you like to ask?")

        if question and st.button("Answer"):
            with st.spinner("Analyzing your image..."):
                answer = moondream.query(image, question)
                st.success("Answer generated")
                st.write(answer)