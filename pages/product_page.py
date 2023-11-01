from .locators_product import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def product_added(self):
        assert ProductPageLocators.MESSAGE in ProductPageLocators.ADD_MESSAGE, "Товар действительно добавлен в корзину"

    def price_is_ok(self):
        assert ProductPageLocators.CURRENT_PRICE in ProductPageLocators.CART_PRICE.text, "Price looks good"

