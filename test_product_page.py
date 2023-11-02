import time

import pytest

from .pages.locators_product import ProductPageLocators
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["0", "1","2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

def test_go_to_product_page(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.product_added()
    page.price_is_ok()

