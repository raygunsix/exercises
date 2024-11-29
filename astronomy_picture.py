import os
from pathlib import Path
import requests
import streamlit as st

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

st.set_page_config(layout="centered")

# Fetch APOD data from NASA API - https://api.nasa.gov/
r = requests.get(url, timeout=10)
content = r.json()

title = content["title"]
explanation = content["explanation"]
image_url = content["url"]

# Fetch image
image_response = requests.get(image_url, timeout=10)
file_name = Path(image_url).name
file_path = f"files/{file_name}"

with open(file_path, "wb") as file:
    file.write(image_response.content)

# Render web page
st.header(title)
st.image(file_path)
st.text(explanation)
