from requests import get
import streamlit as st
st.write(get('https://23110089.streamlit.app/').text)
