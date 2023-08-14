import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    camera_input = st.camera_input("Camera")

if camera_input:

    img = Image.open(camera_input)
    gray_img = img.convert("L")
    st.image(gray_img)