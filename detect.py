import streamlit as st
from PIL import ImageDraw

from constants import page_constants
from helper import get_rectangle_coordinates, random_color, upload_image

def detect_page(moondream):
    st.title(page_constants["detect"]["title"])
    st.write(page_constants["detect"]["subtitle"])
    image = upload_image(page_constants["detect"]["title"])

    if image:
        obj = st.text_input("What do you want to find?")
        if obj and st.button("Find"):
            with st.spinner("Searching..."):
                objects = moondream.detect(image, obj)
                draw = ImageDraw.Draw(image)
                color = random_color()
                for obj in objects:
                    xy = get_rectangle_coordinates(obj, image.size)
                    draw.rectangle(xy, fill=None, outline=color, width=4)
            st.image(image, caption="This is the image with detection")
            st.success("Result generated")