import pytest
import time
from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


# реализация проверки наличия логин ссылки на старице с товаром
def test_guest_should_see_login_link_on_product_page(browser):
    #передаем ссылку для работы
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    #открывает стриницу для использования нужных классов и функций
    page = PageObject(browser, link)
    page.open()
    #выполнение проверки
    page.should_be_login_link()

# маркировка тестов для запуска (- m need_review)
@pytest.mark.need_review
# реализация проверки добалвения товара в корзину не зарегистиривованным пользователем
def test_guest_can_add_product_to_basket(browser):
    # реализация теста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()
    page.add_to_basket_button_click()

# маркировака заведомо падающего теста
@pytest.mark.xfail(reason="expacted failure")
# реализация проверки наличия сообщения после добавления продукта в корзину
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # реализация теста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()

# реализация проверки, что гость не видит сообщение
def test_guest_cant_see_success_message(browser):
    # реализация теста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.test_guest_cant_see_success_message()

@pytest.mark.xfail(reason="expacted failure")
# реализация проверки, что сообщения нет после добавленмя прлдукта в корзину
def test_message_disappeared_after_adding_product_to_basket(browser):
    # реализация теста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = PageObject(browser, link, timeout=10)
    page.open()
    page.add_to_basket_button_click()
    time.sleep(1)
    page.test_message_disappeared_after_adding_product_to_basket()

@pytest.mark.need_review
# реализация проверки наличия товара в корзине
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # реализация теста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link, timeout=10)
    page.open()
    page.go_to_basket_page()
    page.test_product_basket_is_empty()

@pytest.mark.need_review
# реализация проверки возможности перехода на лоин страницц из каталога товаров
def test_guest_can_go_to_login_page_from_product_page(browser):
    # реализация теста
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url,timeout=10)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# класс тестов проверок под зарегистрированным пользователем
class TestUserAddToBasketFromProductPage():
    # реализация setup длф класса тестов
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

    # реализация, что пользоваитель не видит сообщение
    def test_user_cant_see_success_message(self, browser):
        # реализация теста
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = PageObject(browser, link, timeout=10)
        page.open()
        page.test_user_cant_see_success_message()

    @pytest.mark.need_review
    # реализация добавления продукта в корзину
    def test_user_can_add_product_to_basket(self, browser):
        # реализация теста
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = PageObject(browser, link, timeout=10)
        page.open()
        page.add_to_basket_button_click()




