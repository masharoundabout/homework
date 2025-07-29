import os

import pytest
from dotenv import load_dotenv
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

    load_dotenv()
    remote_drv = os.getenv('REMOTE_DRV')
    driver = webdriver.Remote(
        command_executor= remote_drv,
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