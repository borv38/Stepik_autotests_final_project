from .locators_product import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()