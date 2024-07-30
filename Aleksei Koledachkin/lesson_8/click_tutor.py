import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/kg")

login_button = driver.find_element("xpath", '//a[@id="login-desktop"]')
login_button.click()

email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("username@gmail.com")

# print(email_field.get_attribute("value"))
email_field.send_keys("new_username@gmail.com")  # the field will be username@gmail.comnew_username@gmail.com

email_field.clear()

email_field.send_keys("new_username@gmail.com")

time.sleep(2)
