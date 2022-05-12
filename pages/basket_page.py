from .base_page import BasePage
from .locators import BasketPageLocators

basket_url = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert self.browser.current_url == basket_url, \
            f'Expected correct login url: "{basket_url}"'

    def should_be_message_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Empty basket message is not presented'

    def should_not_be_items_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Basket items are presented but should not be'
