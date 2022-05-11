from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_to_basket_button.click()

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            'Add to basket message is not presented'

    def should_be_correct_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_PRODUCT_PAGE), \
            'Item name is not presented (product page)'
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME_BASKET), \
            'Item name is not presented (basket message)'
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_PRODUCT_PAGE).text
        item_name_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_BASKET).text
        assert item_name == item_name_basket, \
            f'Item name (product page): {item_name} should be equal to item name (basket message): {item_name_basket}'

    def should_be_correct_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
            'Item price is not presented'
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), \
            'Basket total is not presented'
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert item_price == basket_price, \
            f'Item price: {item_price} should be equal to basket price: {basket_price}'