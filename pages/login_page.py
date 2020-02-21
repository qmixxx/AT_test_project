from .locators import LoginPageLocators
from .base_page import BasePage
from selenium import webdriver
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert ("login" in self.browser.current_url), "word \"login\" in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is presented"

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        register_email.send_keys(email)
        time.sleep(2)
        register_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        register_pass1.send_keys(password)
        register_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_CONFIRM)
        register_pass2.send_keys(password)
        time.sleep(2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        register_button.click()