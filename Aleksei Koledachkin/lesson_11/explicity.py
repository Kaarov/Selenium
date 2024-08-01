from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/dynamic-properties')

wait = WebDriverWait(driver, 15, poll_frequency=1)

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

VISIBLE_BUTTON = wait.until(EC.presence_of_element_located(VISIBLE_AFTER_BUTTON))
VISIBLE_BUTTON.click()

ENABLE_IN_SECONDS_BUTTON = ("xpath", "//button[@id='enableAfter']")

ENABLE_BUTTON = wait.until(EC.presence_of_element_located(ENABLE_IN_SECONDS_BUTTON))
ENABLE_BUTTON.click()
