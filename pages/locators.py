from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FROM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-noicon div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_HEADER_BUTTON = (By.CSS_SELECTOR, '.header a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")