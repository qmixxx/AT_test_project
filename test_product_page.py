import pytest
import time
from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


#@pytest.mark.parametrize('link', [pytest.param(i, marks=pytest.mark.xfail(i==1, reason='incorrect link')) for i in range(1)])
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_add_product_to_basket(browser):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()
    page.add_to_basket_button_click()
    #page.solve_quiz_and_get_code()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    time.sleep(1)
    page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)

