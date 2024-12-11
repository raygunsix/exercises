import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("data-temp/data.txt")
df.columns=(["datetime", "temp"])

print(df)

figure = px.line(x=df["datetime"], y=df["temp"],
            labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
