from .locators_product import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def product_added(self):
        add_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        assert ProductPageLocators.MESSAGE in add_message.text, "Ошибка"

    def price_is_ok(self):
        cart_price = self.browser.find_element_by_css_selector("#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
        assert ProductPageLocators.CURRENT_PRICE in cart_price.text, "Price not looks good"

