import pytest
from selenium import webdriver


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

