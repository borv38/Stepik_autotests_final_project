from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    CURRENT_PRICE = "9,99"
    CART_PRICE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs")
    MESSAGE = " был добавлен в вашу корзину."
    ADD_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")



