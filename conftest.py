import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.driver.capabilities['enableVNC'] = True
    browser.config.base_url = 'https://demoqa.com'
    yield browser

    browser.quit()




