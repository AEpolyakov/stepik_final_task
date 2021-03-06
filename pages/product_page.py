from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        prod_name_mess = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGES).text
        assert prod_name == prod_name_mess, 'wrong book added to basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "success message is on the page"

    def is_disappear_success(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "success message is not disappeared"
