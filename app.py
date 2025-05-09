from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
import time

# Cấu hình Streamlit
st.title("Truy cập web với Selenium")

# Thiết lập các tùy chọn cho Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Sử dụng WebDriver Manager để tự động tải đúng phiên bản ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Truy cập trang web
driver.get("https://idx.google.com/")
time.sleep(3)

# Lấy tiêu đề trang web và hiển thị
title = driver.title
st.write(f"Tiêu đề của trang web: {title}")

# Đóng trình duyệt sau khi xong
driver.quit()
