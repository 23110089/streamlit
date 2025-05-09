from requests import get
import streamlit as st
st.write(get('https://idx.google.com/').text)
