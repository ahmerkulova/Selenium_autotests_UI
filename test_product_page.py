import pytest
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{offer_num}" for offer_num in range(10)]


@pytest.mark.parametrize('link', [*urls[:7], pytest.param(urls[7], marks=pytest.mark.xfail(reason="Bugged url")), *urls[8:]])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_add_to_basket()
    page.should_be_item_name()
    page.should_be_correct_item_name_basket()
    page.should_be_item_price()
    page.should_be_correct_basket_price()