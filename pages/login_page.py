from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_u = self.browser.current_url
        assert LoginPageLocators.LOGIN_URL in login_u, "Login is not presented in the current URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*BasePageLocators.EM_FIELD)
        email_field.send_keys(email)
        time.sleep(5)
        pass1field = self.browser.find_element(*BasePageLocators.PASS_FIELD)
        pass1field.send_keys(password)
        time.sleep(5)
        pass2field = self.browser.find_element(*BasePageLocators.PASS2_FIELD)
        pass2field.send_keys(password)
        time.sleep(2)
        link = self.browser.find_element(*BasePageLocators.REGISTER)
        link.click()



