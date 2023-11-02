from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_PRICE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") #наименование книги из сообщения о том, что книга добавлена в корзину
    ACTUAL_BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1") #наименование книги




