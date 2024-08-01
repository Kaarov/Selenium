import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://seiyria.com/bootstrap-slider/")

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
EX_2 = driver.find_element(*EX_2_LOCATOR)

# Scroll by selenium
# action.scroll_to_element(EX_2).perform()

# Scroll by JS
scrolls.scroll_to_element(EX_2)

time.sleep(3)
