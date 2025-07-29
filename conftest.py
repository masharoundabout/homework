import pytest
from selenium import webdriver
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.set_capability('browserName', 'chrome')
    chrome_options.set_capability('browserVersion', '126.0')
    chrome_options.set_capability('selenoid:options', {
        'enableVNC': True,
        'enableVideo': True
    })
    chrome_options.enable_bidi = True

    driver = webdriver.Remote(
        command_executor='http://164.92.65.210:4444/wd/hub',
        options=chrome_options
    )

    browser = Browser(Config(driver=driver, timeout=10))
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    attach.add_screenshot(browser)
    #attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()