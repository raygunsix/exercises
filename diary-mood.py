import glob

import nltk
import pandas as pd
import plotly.express as px
import streamlit as st

from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

# Set up
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
moods = []

# Load diary data
filepaths = glob.glob("data-diary/*.txt")
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    filename = Path(filepath).stem
    scores = analyzer.polarity_scores(content)
    moods.append([filename, scores['pos'], scores['neg']])

# Format data
df = pd.DataFrame(moods, columns=['date','pos','neg']) 
df.sort_values(by='date', inplace=True)

# Render data
st.title("Diary Mood")

st.subheader("Positivity")
figure = px.line(x=df['date'], y=df['pos'],
                  labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=df['date'], y=df['neg'],
                  labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)