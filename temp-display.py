import streamlit as st
import plotly.express as px

figure = px.line(x=["2024-01-01", "2024-01-01"], y=[10, 12],
                            labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
