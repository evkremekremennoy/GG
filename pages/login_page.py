from .test_data import TestData
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_in_portal(self):
        self.autorithation_user()
        self.should_be_successful_authorization()

    def should_be_successful_authorization(self):
        # реализовывем проверку, что мы залогинились и наш юзер отображается, как активный
        user_div = self.browser.find_element(*BasePageLocators.USER_NAME)
        user_test = user_div.text
        assert user_test == TestData.user_name, "we have problem with authorization"

    def should_fail_with_wrong_password(self):
        # input credentials of user
        user_name_field = self.browser.find_element(*LoginPageLocators.USER_NAME)
        user_name_field.click()
        user_name_field.send_keys(TestData.user_name)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.click()
        password_field.send_keys(TestData.password + "1")
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def should_fail_with_wrong_username(self):
        # input credentials of user
        user_name_field = self.browser.find_element(*LoginPageLocators.USER_NAME)
        user_name_field.click()
        user_name_field.send_keys(TestData.user_name + "1")
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.click()
        password_field.send_keys(TestData.password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def should_not_be_user_name_in_header(self):
        assert self.is_not_element_present(*BasePageLocators.USER_NAME), "User login with wrong credentials"

    def should_be_change_password_to_One_time_password(self):
        self.browser.find_element(*LoginPageLocators.CHECKBOX_ONE_TIME_PASSWORD).click()
        assert self.is_element_present(*LoginPageLocators.PASSWORD_ONE_TIME), "checkbox 'Connect with support user " \
                                                                              "one-time password' doesn't change type of password"

    def should_fail_using_passwor_in_one_time_password_field(self):
        self.browser.find_element(*LoginPageLocators.CHECKBOX_ONE_TIME_PASSWORD).click()
        user_name_field = self.browser.find_element(*LoginPageLocators.USER_NAME)
        user_name_field.click()
        user_name_field.send_keys(TestData.user_name)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_ONE_TIME)
        password_field.click()
        password_field.send_keys(TestData.password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()
        assert self.is_element_present(*LoginPageLocators.INVALID_OTP), "system used the regular password as one-time"
