import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "XX.XX.XXX.XXX:XXXX"  # username:password@XX.XX.XXX.XXX:XXXX

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")
driver = webdriver.Chrome(options=options)

driver.get("https://2ip.ru")

time.sleep(2)
