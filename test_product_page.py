import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link_visible = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
link_login = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


@pytest.mark.registered
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/accounts/login/')
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", 'test_pass')
        page.should_be_authorized()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail)])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_visible)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_visible)
    page.open()
    page.add_product_to_basket()
    page.is_disappear_success()


def test_guest_should_see_login_link_on_product_page(browser):
    local_link = link_login
    page = ProductPage(browser, local_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    local_link = link_login
    page = ProductPage(browser, local_link)
    page.open()
    page.go_to_login_page()
    page.is_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_is_empty_message()
