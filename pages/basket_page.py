from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def test_product_basket_is_empty(self):
        check_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "empty" in check_text, "the basket is not empty"



