import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.capabilities['enableVNC'] = True
    yield browser

    browser.quit()




