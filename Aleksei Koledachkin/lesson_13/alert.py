import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

BUTTON_ALERT = ("xpath", "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_ALERT)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.accept()

BUTTON_ALERT_CONFIRM = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_ALERT_CONFIRM)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
print(alert.text)
alert.dismiss()
time.sleep(3)

BUTTON_ALERT_PROMT = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_ALERT_PROMT)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.send_keys("Promt Alert!")
alert.accept()
time.sleep(3)
