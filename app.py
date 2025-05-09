import streamlit as st
import streamlit.components.v1 as components

st.title("Nhúng web trong Streamlit")
components.iframe("https://idx.google.com/", height=600)
