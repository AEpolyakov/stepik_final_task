from selenium.webdriver.common.by import By
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
        assert self.is_element_present(By.ID, 'login_form'), 'no login form on login page'

    def should_be_register_form(self):
        assert self.is_element_present(By.ID, 'register_form'), 'no register form on login page'
