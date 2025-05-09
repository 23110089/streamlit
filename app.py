from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get("https://idx.google.com/"); time.sleep(3)
title = driver.title
st.write(f"Tiêu đề của trang web: {title}")
driver.quit()
