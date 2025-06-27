import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
# from dotenv import load_dotenv
from tests.utils import attach

DEFAULT_BROWSER_VERSION = "128.0"
def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )




@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    # options = Options()
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = webdriver.ChromeOptions()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
        "goog:loggingPrefs": {"browser": "ALL"}
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.driver.maximize_window()

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()