from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
      #  self.should_be_login_form()
       # self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url.Contains(*LoginPageLocators.LOGIN_URL), "Login is not presented in the current URL"
#
#   # def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
 #       assert True
#
  #  def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
   #     assert True