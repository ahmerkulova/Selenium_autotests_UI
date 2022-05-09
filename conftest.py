import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Browser option needed: chrome, firefox')
    parser.addoption('--language', action='store', default='en',
                     help='User language option needed: ru, en, es, fr and others')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if user_language:
        if browser_name == 'chrome':
            print('\nstarting Chrome browser')
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            print('\nstarting Firefox browser')
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError('--browser_name should be chrome or firefox')
    else:
        raise pytest.UsageError('--language should be specified')
    yield browser
    print('\nquiting browser')
    browser.quit()