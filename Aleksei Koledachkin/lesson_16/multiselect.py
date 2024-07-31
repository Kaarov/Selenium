from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/select-menu")

# SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")
# driver.find_element(*SELECT_LOCATOR).send_keys("Ms." + Keys.ENTER)

# SELECT1 = ("xpath", "//div[@id='selectOne']")
# PROF_OPTION = ("xpath", "//div[text()='Prof.']")
# driver.find_element(*SELECT1).click()
# driver.find_element(*PROF_OPTION).click()

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")
driver.find_element(*MULTISELECT_LOCATOR).send_keys("Gre" + Keys.TAB + Keys.ENTER)
