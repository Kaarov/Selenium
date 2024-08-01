import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

# Step 1 Easy way
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# COLUMN_A = ("xpath", "//div[@id='column-a']")
# COLUMN_B = ("xpath", "//div[@id='column-b']")

# A = driver.find_element(*COLUMN_A)
# B = driver.find_element(*COLUMN_B)

# time.sleep(3)
# action.drag_and_drop(A, B).perform()
# time.sleep(3)


# Step 2 Hard Way
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")
# JS debug: setTimeout(function() { debugger; }, 5000);

GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")

action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()

time.sleep(5)
