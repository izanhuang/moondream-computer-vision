import streamlit as st

from constants import page_constants
from helper import upload_image

def caption_page(moondream):
    st.title(page_constants["caption"]["title"])
    st.write(page_constants["caption"]["subtitle"])
    image = upload_image(page_constants["caption"]["title"])

    if image:
        length = st.radio("Select the caption length", ["Short", "Normal", "Long"], horizontal=True).lower()
        if st.button("Generate caption"):
            with st.spinner("Analyzing your image..."):
                caption = moondream.caption(image, length)
                st.success("Caption created")
                st.write(caption)