from .locators_product import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def product_added(self):
        a_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        print(a_message.text)
        full_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print("Название книги: " + full_book_name.text)
        #row_to_compare = full_book_name.text + " был добавлен в вашу корзину."
        assert ProductPageLocators.MESSAGE in a_message.text, "Ошибка"
        print("Товар добавлен успешно")

    def price_is_ok(self):
        c_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        assert ProductPageLocators.CURRENT_PRICE in c_price.text, "Price not looks good"
        print("Стоимость товара в корзине соответствует стоимости товара")
