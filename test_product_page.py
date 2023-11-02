import time

import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.locators_product import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


# @pytest.mark.parametrize('link',
#                          ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
# def test_go_to_product_page(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     time.sleep(10)
#     page.product_added()
#     page.price_is_ok()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_cart()
#     page.should_not_be_success_message()
#
#
# def test_guest_can_add_product_to_basket(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_cart()
#     time.sleep(5)
#     page.product_added()


# def test_guest_cant_see_success_message(self, browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_cart()
#     page.should_be_disappeared()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_the_cart()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.checkout_button_exists()
#     basket_page.empty_cart()


@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "alladinEr6")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)
        page.add_to_cart()
        time.sleep(5)
        page.product_added()
