import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://the-internet.herokuapp.com/upload")

upload_field = driver.find_element("xpath", "//input[@type='file' and @id='file-upload']")
upload_field.send_keys(f"{os.getcwd()}/downloads/black.png")

time.sleep(3)
