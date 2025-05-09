from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st
import time

# Cấu hình Streamlit
st.title("Truy cập web với Selenium")

# Nhập URL từ người dùng
url = st.text_input("Nhập URL của website muốn truy cập", "https://example.com")

# Tạo nút để chạy Selenium
if st.button("Truy cập web"):
    # Cấu hình trình duyệt Chrome (Headless Mode)
    options = Options()
    options.headless = True  # Chạy trình duyệt mà không mở cửa sổ

    # Đường dẫn đến ChromeDriver
    driver = webdriver.Chrome(options=options)

    # Truy cập trang web
    driver.get(url)
    
    # Đợi trang load hoàn chỉnh (có thể thay đổi thời gian này tùy theo tốc độ load của trang)
    time.sleep(3)
    
    # Lấy tiêu đề trang web
    title = driver.title
    st.write(f"Tiêu đề của trang web: {title}")
    
    # Lấy nội dung của trang (ví dụ: lấy tất cả các thẻ <p>)
    paragraphs = driver.find_elements_by_tag_name("p")
    for para in paragraphs:
        st.write(para.text)
    
    # Đóng trình duyệt sau khi xong
    driver.quit()
