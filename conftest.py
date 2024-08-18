import pytest
from selenium import webdriver
import settings


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Unknown browser: {request.param}')
    yield driver
    driver.quit()


class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if browserName == 'firefox':
            return webdriver.firefox()
        elif browserName == 'chrome':
            return webdriver.Chrome()
    @pytest.fixture(scope='function')
    def driver_f():
        firefox_driver = webdriver.Firefox()
        firefox_driver.get(settings.URL)
        firefox_driver.maximize_window()

        yield firefox_driver

        firefox_driver.quit()

    @pytest.fixture(scope='function')
    def driver_c():
        chrome_driver = webdriver.Chrome()
        chrome_driver.get(settings.URL)

        yield chrome_driver

        chrome_driver.quit()
