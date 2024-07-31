import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/global/kg/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver.find_element(*LOGIN_FIELD).send_keys("Login")
driver.find_element(*PASSWORD_FIELD).send_keys("Password")
driver.find_element(*LOGIN_FIELD).click()

# Save cookies
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()

# Work with saved cookies
cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
