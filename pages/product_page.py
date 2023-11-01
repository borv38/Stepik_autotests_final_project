from .locators_product import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def product_added(self):
        a_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        assert ProductPageLocators.MESSAGE in a_message.text, "Ошибка"

    def price_is_ok(self):
        c_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        assert ProductPageLocators.CURRENT_PRICE in c_price.text, "Price not looks good"

