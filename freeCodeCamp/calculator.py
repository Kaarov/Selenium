from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="../chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.marshu.com/articles/calculate-addition-calculator-add-two-numbers.php")
driver.maximize_window()
driver.implicitly_wait(3)

try:
    no_button = driver.find_element(By.CLASS_NAME, "milo-animation delay-4")
    no_button.click()
except:
    print("No element with this element. Skipping ...")

sum1 = driver.find_element(By.CSS_SELECTOR, 'input[name="n01"]')
sum2 = driver.find_element(By.CSS_SELECTOR, 'input[name="n02"]')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

time.sleep(3)

btn = driver.find_element(By.CSS_SELECTOR, 'input[onclick="findcalculatorcalculate(this.form)"]')
btn.click()

time.sleep(3)
