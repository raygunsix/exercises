import streamlit as st
import plotly.express as px

st.title("In Search of Happiness")
xaxis = st.selectbox("Select the data for the X-axis",
             ("GDP", "Happiness", "Generosity"))
yaxis = st.selectbox("Select the data for the Y-axis",
             ("GDP", "Happiness", "Generosity"))

st.subheader(f"{xaxis} and {yaxis}")

figure = px.scatter(x=[0,1,3,5], y=[3,4,5,6],
                 labels={"x": xaxis, "y": yaxis})
st.plotly_chart(figure)