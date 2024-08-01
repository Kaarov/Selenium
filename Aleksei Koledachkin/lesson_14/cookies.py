from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/global/kg")

# print(driver.get_cookie("country_code"))
# print(driver.get_cookies())

# driver.add_cookie({
#     "name": "Example",
#     "value": "Cookies"
# })

# print(driver.get_cookie("Example"))

cookie_before = driver.get_cookie("split")
print(cookie_before)

# driver.delete_cookie("split")
driver.delete_all_cookies()

driver.add_cookie({
    "name": "split",
    "value": "QWERTY",
})

cookie_after = driver.get_cookie("split")
print(cookie_after)
