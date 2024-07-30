import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/login")

login_button = driver.find_element(By.ID, "loginformsubmit")
# print(driver.find_element("id", "loginformsubmit"))

print(login_button)
login_button.click()

time.sleep(2)
