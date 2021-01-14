from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FROM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()

        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        repeat_password_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password)

        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()



