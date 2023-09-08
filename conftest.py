import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()