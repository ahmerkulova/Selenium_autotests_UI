from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert item_price == basket_price, \
            f'Item price: {item_price} should be equal to basket price: {basket_price}'

    def should_be_correct_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_PRODUCT_PAGE).text
        item_name_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_BASKET).text
        assert item_name == item_name_basket, \
            f'Item name (product page): {item_name} should be equal to item name (basket): {item_name_basket}'