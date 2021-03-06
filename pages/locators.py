from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a[contains(@href,'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    REGISTER_EMAIL_ADDRESS = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_NAME_IN_MESSAGES = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]//strong')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"]')


class BasketPageLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
    PRODUCTS = (By.XPATH, '//div[@class="basket-items"]')

