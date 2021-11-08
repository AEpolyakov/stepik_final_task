from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'not a login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no login form on login page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'no register form on login page'

    def register_new_user(self, email, password):
        self.send_keys_to_element(email, *LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        self.send_keys_to_element(password, *LoginPageLocators.REGISTER_PASSWORD1)
        self.send_keys_to_element(password, *LoginPageLocators.REGISTER_PASSWORD2)
        self.button_click(*LoginPageLocators.REGISTER_BUTTON)
