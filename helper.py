import random
import streamlit as st
from PIL import Image

def random_color(): 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def get_rectangle_coordinates(obj, image_size):
    width =  image_size[0]
    height =  image_size[1]
    x_min = obj["x_min"] * width
    y_min = obj["y_min"] * height
    x_max = obj["x_max"] * width
    y_max = obj["y_max"] * height
    return [x_min, y_min, x_max, y_max]

def upload_image(page):
    uploaded_file = st.file_uploader("Upload an image", ["jpg", "png", "jpeg"], key=page)
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="This is the image you uploaded")
        return image
    return None