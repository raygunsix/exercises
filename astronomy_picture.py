import os
import requests
import streamlit as st

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

st.set_page_config(layout="centered")

# Fetch APOD data from NASA API
# https://api.nasa.gov/
r = requests.get(url, timeout=10)
content = r.json()
print(r)

title = content["title"]
explanation = content["explanation"]

# Render web page
st.header(title)

st.text(explanation)
