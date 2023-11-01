from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    CURRENT_PRICE = "9,99"
    #MESSAGE = " был добавлен в вашу корзину."
    MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/text()')
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CART_PRICE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")



