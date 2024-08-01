import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown")

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

# DROPDOWN.select_by_visible_text("Option 1")
# DROPDOWN.select_by_value("2")
# DROPDOWN.select_by_index(1)

all_options = DROPDOWN.options
for option in all_options:
    # DROPDOWN.select_by_visible_text(option.text)
    # DROPDOWN.select_by_index(all_options.index(option))
    DROPDOWN.select_by_value(option.get_attribute("value"))
    time.sleep(1)
