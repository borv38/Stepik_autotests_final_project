import time

from .pages.locators_product import ProductPageLocators
from .pages.product_page import ProductPage

def test_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.product_added()
    page.price_is_ok()






