from requests import get
from time import sleep
import streamlit as st

while True:
  sleep(10)
  st.write(get('https://23110089.streamlit.app/').text)
