from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be before adding item to basket'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is not disappeared after adding item to basket'

    def add_product_to_basket(self):
        add_product_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_to_basket_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message after adding to basket is not presented'

    def should_be_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_PRODUCT_PAGE), \
            'Item name is not presented (product page)'

    def should_be_correct_item_name_basket(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_BASKET), \
            'Item name is not presented (basket message)'
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_PRODUCT_PAGE).text
        item_name_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_BASKET).text
        assert item_name == item_name_basket, \
            f'Item name (product page): {item_name} should be equal to item name (basket message): {item_name_basket}'

    def should_be_item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
            'Item price is not presented'

    def should_be_correct_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), \
            'Basket total is not presented'
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert item_price == basket_price, \
            f'Item price: {item_price} should be equal to basket price: {basket_price}'