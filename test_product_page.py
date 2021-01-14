from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_added_product_name(product_name)
    page.check_added_product_price(product_price)



