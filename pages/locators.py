from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_incorrect')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_INPUT_REG = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT_REG = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMATION_INPUT_REG = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ITEM_NAME_PRODUCT_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_NAME_BASKET = (By.CSS_SELECTOR, '.alertinner strong')