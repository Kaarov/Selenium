from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_ratings):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_rating in star_ratings:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHtml')).strip() == f'{star_rating} star':
                    star_element.click()
                    break
