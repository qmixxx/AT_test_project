from .base_page import BasePage
from .locators import PageObjectLocators
import time

class PageObject(BasePage):
    # реализуйте проверку наличия кнопки
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*PageObjectLocators.ADD_TO_BASKET), "Button is presented"

    def add_to_basket_button_click(self):
        add_button = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        add_button.click()
        #time.sleep(2)



