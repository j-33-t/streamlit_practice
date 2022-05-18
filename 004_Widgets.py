import streamlit as st

st.title("Slider Widget")

x = st.slider('x')# 👈 this is a widget

st.write(x, 'squared is', x * x)

