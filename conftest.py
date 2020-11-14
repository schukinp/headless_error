import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import config, browser


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(options=options)
browser.set_driver(driver)
driver.maximize_window()
config.timeout = 15


@pytest.fixture(autouse=True)
def setup():
    browser.open_url('https://www.google.com')
    yield
    browser.quit()
