import pandas as pd
import plotly.express as px
import streamlit as st

st.title("In Search of Happiness")
xaxis = st.selectbox("Select the data for the X-axis",
             ("GDP", "Happiness", "Generosity"))
yaxis = st.selectbox("Select the data for the Y-axis",
             ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("data-happy/happy.csv")

match xaxis:
    case "GDP":
        xdata = df['gdp']
    case "Happiness":
        xdata = df['happiness']
    case "Generosity":
        xdata = df['generosity'] 

match yaxis:
    case "GDP":
        ydata = df['gdp']
    case "Happiness":
        ydata = df['happiness']
    case "Generosity":
        ydata = df['generosity'] 

st.subheader(f"{xaxis} and {yaxis}")

figure = px.scatter(x=xdata, y=ydata,
                 labels={"x": xaxis, "y": yaxis})
st.plotly_chart(figure)