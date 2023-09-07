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
        self.should_be_advansed()
        self.should_be_login_with_regisered_user()
        #self.should_be_successful_authorization()

    def should_be_advansed(self):
        #open page when browser warns about the danger of opening the page
        try:
            adv_button = self.browser.find_element(*LoginPageLocators.ADVANCED_BUTTON).click()
            proceed_button = self.browser.find_element(*LoginPageLocators.PROCEED_TO_PORTAL_BUTTON).click()
        except:
            pass

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
        time.sleep(5)
        logs = self.browser.get_log('browser')
        # Шукаємо URL в журналі
        for log in logs:
            if 'Failed to load resource' in log['message']:
                match = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                  log['message'])
                print("TEXT MESSAGE = ", log['message'])
                if match:
                    url = match.group()
                    # Відкриваємо нову вкладку
                    self.browser.execute_script("window.open('', '_blank');")
                    # Переключаємося на нову вкладку
                    self.browser.switch_to.window(self.browser.window_handles[1])
                    # Тут ви можете використовувати URL, наприклад, відкрити його в браузері
                    self.browser.get(url)
                    #allow to use this api
                    self.should_be_advansed()
                    self.browser.switch_to.window(self.browser.window_handles[0])

        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def should_be_successful_authorization(self):
        # реализовывем проверку, что мы залогинились и наш юзер отображается, как активный
        user_div = self.browser.find_element(*BasePageLocators.USER_NAME)
        user_test = user_div.text
        assert user_test == TestData.user_name, "we have problem with authorization"
