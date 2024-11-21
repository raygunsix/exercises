# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

def convert_to_grayscale(image):
    """ converts a image to grayscale """
    img = Image.open(image)
    graysacle_img = img.convert('L')
    return graysacle_img


st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    grayscale_img = convert_to_grayscale(camera_image)
    st.image(grayscale_img)

if uploaded_image:
    grayscale_img = convert_to_grayscale(uploaded_image)
    st.image(grayscale_img)    

# st.session_state