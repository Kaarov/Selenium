import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path="chromedriver", teardown=False):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_sign_in_info(self):
        close_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        close_button.click()

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        selected_currency_element = self.find_elements(By.CSS_SELECTOR, "div.b284c0e8fc")
        for element in selected_currency_element:
            if element.text == currency:
                element.click()

    def select_place_to_go(self, place_to_go=None):
        search_field = self.find_element(By.ID, ":rh:")
        search_field.clear()
        search_field.send_keys(place_to_go, Keys.ENTER)

    def select_dates(self, check_in_date=None, check_out_date=None):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[aria-controls=":rl:"]')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR,
                'button[class="dba1b3bddf e99c25fd33 aabf155f9a f42ee7b31a a86bcdb87f e137a4dfeb af4d87ec2f"]'
            )
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.ID, "group_adults")
            adults_value = adults_value_element.get_attribute("value")
            if int(adults_value) == 1:
                break
        increase_adults_element = self.find_elements(
            By.CSS_SELECTOR,
            'button[class="dba1b3bddf e99c25fd33 aabf155f9a f42ee7b31a a86bcdb87f e137a4dfeb d1821e6945"]'
        )
        for _ in range(count - 1):
            increase_adults_element[0].click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(self)
        filtration.apply_star_rating(3, 4, 5)
