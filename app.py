from requests import get
from time import sleep
import streamlit as st

out = st.empty()
while True:
  sleep(10)
  out.empty()
  out.write(get('https://23110089.streamlit.app/').text)
