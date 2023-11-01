import time

from pages.locators_product import ProductPageLocators
from .pages.product_page import ProductPage

def test_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    print(ProductPageLocators.MESSAGE)
    print(ProductPageLocators.ADD_MESSAGE)
    time.sleep(3)
    page.product_added()
    page.price_is_ok()






