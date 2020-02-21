import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

# маркировка тестов для запуска (- m login_guest)
@pytest.mark.login_guest
# класс тестов работы с формой на странице лоигна
class TestLoginFromMainPage():
    # реализация, что пользоваитель не видит сообщение
    # передаем первым аргументом self
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
         # реализация теста
         url = "http://selenium1py.pythonanywhere.com/"
         page = MainPage(browser, url,timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
         page.open()  # открываем страницу
         page.go_to_login_page()
         login_page = LoginPage(browser, browser.current_url)
         login_page.should_be_login_page()

    # реализация, что пользоваитель не видит сообщение
    def test_guest_should_see_login_link(self, browser):
        # реализация теста
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url, timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()

# маркировака теста, который будет пропущен
@pytest.mark.skip
# реализация, проверки логин формы
def test_guest_check_login_form_register_form(browser):
    # реализация теста
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, url, timeout=10)
    # открываем страницу
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

# реализация, проверки что гость не видит товар в корзине при переходе с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # реализация теста
    url = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, url, timeout=10)
    page.open()
    page.go_to_basket_page()
    page.test_product_basket_is_empty()






