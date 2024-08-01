import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/checkboxes")

CHECKBOX1 = ("xpath", "(//input[@type='checkbox'])[1]")

time.sleep(2)
print(driver.find_element(*CHECKBOX1).get_attribute("checked"))  # None: None
driver.find_element(*CHECKBOX1).click()
print(driver.find_element(*CHECKBOX1).get_attribute("checked"))  # true: str
time.sleep(2)
driver.refresh()
print(driver.find_element(*CHECKBOX1).is_selected())  # False: bool
driver.find_element(*CHECKBOX1).click()
print(driver.find_element(*CHECKBOX1).is_selected())  # True: bool
time.sleep(2)
