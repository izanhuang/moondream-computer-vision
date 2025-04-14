import streamlit as st
from moondream_lib import MoondreamHelper
from page import page_handlers, page_titles

st.set_page_config(
    page_title="Moondream Dashboard",
    page_icon="🌙"
)

@st.cache_resource
def get_moondream():
    return MoondreamHelper(api_key=st.secrets["moondream_api_key"])

moondream = get_moondream()


st.sidebar.title("🌙 Moondream Vision API")

current_page_title = st.sidebar.radio("Select the page you want to visit", page_titles)

page_handlers[current_page_title](moondream)
