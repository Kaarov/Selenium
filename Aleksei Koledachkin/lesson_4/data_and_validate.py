import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

current_url = driver.current_url
print("Current URL: ", current_url)
assert current_url == "https://www.wikipedia.org/", "Error in URL"

current_title = driver.title
print("Current Title: ", current_title)
assert current_title == "Wikipedia", "Error in Title"

# print(driver.page_source)

time.sleep(2)
