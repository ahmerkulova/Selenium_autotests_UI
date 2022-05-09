from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        correct_url = f'{self.url}en-gb/accounts/login/'
        MainPage.go_to_login_page(self)
        assert self.browser.current_url == correct_url, \
            f"Expected correct login url: {correct_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True
        pass

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
