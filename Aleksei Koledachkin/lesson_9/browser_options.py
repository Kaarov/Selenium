import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
# chrome_option.add_argument('--incognito')
# chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_argument('--window-size=1920, 1080')
# chrome_option.add_argument('--disable-cache')
# chrome_option.page_load_strategy = "normal"
chrome_option.page_load_strategy = "eager"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)

# driver.set_window_size(1920, 1080)

start_time = time.time()

driver.get('https://whatismyipaddress.com/ru/index')

end_time = time.time()

print(f"The result: {end_time - start_time}")
