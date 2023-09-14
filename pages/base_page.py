from .test_data import TestData

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def autorithation_user(self):
        # input credentials of user
        user_name_field = self.browser.find_element(*LoginPageLocators.USER_NAME)
        user_name_field.click()
        user_name_field.send_keys(TestData.user_name)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.click()
        password_field.send_keys(TestData.password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        finally:
            return True

    #Old
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.USER_NAME), "Login link is not presented"