import pytest
import faker

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
link_item2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
quiz_offer_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
urls = [f"{link}/?promo=offer{offer_num}" for offer_num in range(10)]


# @pytest.mark.parametrize('link', [*urls[:7], pytest.param(urls[7], marks=pytest.mark.xfail(reason="Bugged url")), *urls[8:]])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):  # add link here as a parameter to parametrize
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()  # only for quiz_offer_link
    page.should_be_success_message()
    page.should_be_item_name()
    page.should_be_correct_item_name_basket()
    page.should_be_item_price()
    page.should_be_correct_basket_price()


@pytest.mark.negative
@pytest.mark.skip(reason='Correct behavior')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.negative
@pytest.mark.xfail(reason='Message should not disappear for current version of the page')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_item2)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_item2)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_item2)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_empty_basket()
    basket_page.should_be_message_in_empty_basket()


@pytest.mark.reg_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        self.email = f.email()
        self.password = f.password()
        page = ProductPage(browser, link_item2)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(self.email, self.password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_success_message()
        page.should_be_item_name()
        page.should_be_correct_item_name_basket()
        page.should_be_item_price()
        page.should_be_correct_basket_price()
