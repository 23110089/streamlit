from requests import get
from time import sleep
from streamlit import empty; out = empty()

out.empty(); out.write('há há')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Khởi động trình duyệt
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mở trang web
driver.get("https://www.google.com")

# Tìm ô tìm kiếm và nhập từ khóa
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Selenium")
search_box.submit()
