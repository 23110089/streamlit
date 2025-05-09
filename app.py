from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st
import time

# Nhập URL từ người dùng
url = st.text_input("Nhập URL của website muốn truy cập", "https://example.com")

# Tạo nút để chạy Selenium
if st.button("Truy cập web"):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://idx.google.com/"); time.sleep(3)
    title = driver.title
    st.write(f"Tiêu đề của trang web: {title}")
    driver.quit()
