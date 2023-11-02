from .locators_product import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def product_added(self):
        # a_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE)
        # print(a_message.text)
        a_book_name = self.browser.find_element(*ProductPageLocators.ACTUAL_BOOK_NAME)
        full_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert a_book_name.text == full_book_name.text, "Ошибка"
        print("Товар добавлен успешно")

    def price_is_ok(self):
        c_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        subj_price = self.browser.find_element(*ProductPageLocators.PRICE)
        print(subj_price.text[1:])
        print(c_price.text)
        assert subj_price.text[1:] in c_price.text, "Price not looks good"
        print("Стоимость товара в корзине соответствует стоимости товара")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), \
            "Nothing to wait"

