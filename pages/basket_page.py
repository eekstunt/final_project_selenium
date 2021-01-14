from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, link):
        self.browser = browser
        self.url = link

    def check_whether_basket_is_empty(self):
        assert 'пуста' or 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text