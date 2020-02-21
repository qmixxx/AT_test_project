from .base_page import BasePage
from .login_page import LoginPage
from .locators import PageObjectLocators
import time
import random

class PageObject(BasePage):
    # реализуйте проверку наличия кнопки
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*PageObjectLocators.ADD_TO_BASKET), "Button is presented"

    def add_to_basket_button_click(self):
        add_button = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        add_button.click()
        #time.sleep(2)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"
        #succ_message = self.browser.find_element(*PageObjectLocators.SUCCESS_MESSAGE).text

    def test_guest_cant_see_success_message(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"

    def test_user_cant_see_success_message(self):
         # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"

    def test_message_disappeared_after_adding_product_to_basket(self):
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        assert self.is_disappeared(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"


