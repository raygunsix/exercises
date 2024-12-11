import plotly.express as px
import sqlite3
import streamlit as st

connection = sqlite3.connect("temp.sqlite3")
cursor = connection.cursor()
dates = []
temps = []

cursor.execute("SELECT date, temp FROM temps")
rows = cursor.fetchall()

for row in rows:
    dates.append(row[0])
    temps.append(row[1])

figure = px.line(x=dates, y=temps,
            labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
