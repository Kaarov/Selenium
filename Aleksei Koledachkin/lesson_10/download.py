import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
prefs = {"download.default_directory": f"{os.getcwd()}/downloads"}
chrome_option.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

driver.get("https://the-internet.herokuapp.com/download")

driver.find_elements("xpath", "//a")[2].click()

time.sleep(5)
