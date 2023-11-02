from selenium.webdriver.common.by import By


# class MainPageLocators():
#  LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#content_inner > div.form-group.clearfix > div > div > a")
    EMPTY_CART_PROOF = (By.CSS_SELECTOR, "#content_inner > p")
