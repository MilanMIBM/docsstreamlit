import streamlit as st
import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

st.plotly_chart(fig, key="iris", on_select="rerun")

st.session_state.iris
