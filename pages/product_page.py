from .base_page import BasePage
from .locators import ProductPageLocators
from ..utils import format_number

class ProductPage(BasePage):
    def __init__(self, browser, link):
        self.browser = browser
        self.url = link

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "add to basket button is not presented"

    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_added_product_name(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text, "wrong product name"

    def check_added_product_price(self, product_price):
        assert format_number(product_price) == format_number(self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text), "wrong product price"
