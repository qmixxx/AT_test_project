from .base_page import BasePage
from .locators import PageObjectLocators

#определение класса для работы со страницей. Наследует класс BasePage
class PageObject(BasePage):
    # реализация проверки наличия кнопки
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*PageObjectLocators.ADD_TO_BASKET), "Button is presented"

    # реализация нажатия на кнопку добавления в корзину
    def add_to_basket_button_click(self):
        add_button = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        add_button.click()

    # реализация проверки наличия сообщения после добавления продукта в корзину
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"
        #succ_message = self.browser.find_element(*PageObjectLocators.SUCCESS_MESSAGE).text

    # реализация проверки, что гость не видит сообщение
    def test_guest_cant_see_success_message(self):
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"

    # реализация, что пользоваитель не видит сообщение
    def test_user_cant_see_success_message(self):
         # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"

    # реализация проверки, что сообщения нет после добавленмя прлдукта в корзину
    def test_message_disappeared_after_adding_product_to_basket(self):
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        assert self.is_disappeared(*PageObjectLocators.SUCCESS_MESSAGE), "text is not presented"


