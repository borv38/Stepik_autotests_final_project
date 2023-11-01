from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    CURRENT_PRICE = "9,99"
    MESSAGE = " был добавлен в вашу корзину."
    ADD_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/text()')



