from .pages.main_page import MainPage, LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_from_header()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET)
    basket_page.check_whether_basket_is_empty()



