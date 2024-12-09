import glob
import plotly.express as px
import streamlit as st

st.title("Diary Mood")

# Load diary data
filepaths = glob.glob("data-diary/*.txt")
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()

st.subheader("Positivity")

st.subheader("Negativity")