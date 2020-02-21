import pytest
import time
from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
#from .pages.base_page import BasePage


#@pytest.mark.parametrize('link', [pytest.param(i, marks=pytest.mark.xfail(i==1, reason='incorrect link')) for i in range(1)])
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()
    page.add_to_basket_button_click()
    #page.solve_quiz_and_get_code()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    time.sleep(1)
    page.test_message_disappeared_after_adding_product_to_basket()

#@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link, timeout=10)
    page.open()
    page.go_to_basket_page()
    page.test_product_basket_is_empty()

#@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # реализация теста
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url,timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Задаем значения для email и password
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, url, timeout=10)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = PageObject(browser, link, timeout=10)
        page.open()
        page.test_user_cant_see_success_message()

    #@pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = PageObject(browser, link, timeout=10)
        page.open()
        page.add_to_basket_button_click()
        # page.solve_quiz_and_get_code()



