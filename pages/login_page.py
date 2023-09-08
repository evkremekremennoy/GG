from .test_data import TestData
import time
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_in_portal(self):
        self.should_be_login_with_regisered_user()
        self.should_be_successful_authorization()

    def should_be_login_with_regisered_user(self):
        wait = WebDriverWait(self.browser, 10)
        #input credentials of user
        user_name_field = self.browser.find_element(*LoginPageLocators.USER_NAME)
        user_name_field.click()
        user_name_field.send_keys(TestData.user_name)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.click()
        password_field.send_keys(TestData.password)
        #open console
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def should_be_successful_authorization(self):
        # реализовывем проверку, что мы залогинились и наш юзер отображается, как активный
        user_div = self.browser.find_element(*BasePageLocators.USER_NAME)
        user_test = user_div.text
        assert user_test == TestData.user_name, "we have problem with authorization"
