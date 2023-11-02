from .base_page import BasePage
from .locators import BasePageLocators


# Методы для проверки корзины - добавил сюда
class BasketPage(BasePage):

    def checkout_button_exists(self):
        assert self.is_not_element_present(*BasePageLocators.CHECKOUT_BUTTON), \
            "The cart is not empty"

    def empty_cart(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_CART_PROOF), \
            "There is no message that cart is an empty"
