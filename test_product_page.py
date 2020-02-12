import pytest
from .pages.product_page import PageObject




@pytest.mark.parametrize('link', [pytest.param(i, marks=pytest.mark.xfail(i==1, reason='incorrect link')) for i in range(2)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    page.solve_quiz_and_get_code()
    
