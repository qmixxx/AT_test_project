from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url, timeout=10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина

def test_guest_check_login_form_register_form(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url, timeout=10)
    page.open()  # открываем страницу
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()




