from .base_page import BasePage
from .locators import LoginPageLocators

login_url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == login_url, \
            f'Expected correct login url: "{login_url}"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not presented'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REG)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REG)
        password_input.send_keys(password)
        password_confirmation_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_INPUT_REG)
        password_confirmation_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
