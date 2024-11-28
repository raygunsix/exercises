import os
import requests
import streamlit as st

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

st.set_page_config(layout="centered")

# Fetch APOD data from NASA API
# https://api.nasa.gov/
r = requests.get(url)

print(r)

# Render web page


st.title("Title")

st.text("text")