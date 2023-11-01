from pages.base_page import BasePage
from pages.locators_product import ProductPageLocators


class add_prod_to_basket(BasePage):
    def compare_message(self):
        self.price_is_ok()
        self.product_added()

    def price_is_ok(self):
        assert ProductPageLocators.CURRENT_PRICE in ProductPageLocators.CART_PRICE.text, "Price looks good"

    def product_added(self):
        assert ProductPageLocators.MESSAGE in ProductPageLocators.ADD_MESSAGE, "Товар действительно добавлен в корзину"
