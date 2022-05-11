from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ITEM_NAME_PRODUCT_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_NAME_BASKET = (By.CSS_SELECTOR, '.alertinner strong')