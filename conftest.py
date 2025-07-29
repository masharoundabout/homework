import pytest
from selenium import webdriver
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.set_capability('browserName', 'chrome')
    chrome_options.set_capability('browserVersion', '126.0')
    chrome_options.set_capability('selenoid:options', {
        'enableVNC': True,
        'enableVideo': True
    })
    chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    driver = webdriver.Remote(
        command_executor='http://164.92.65.210:4444/wd/hub',
        options=chrome_options
    )

    browser = Browser(Config(driver=driver, timeout=10))
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    browser.quit()