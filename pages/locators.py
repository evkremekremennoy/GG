from selenium.webdriver.common.by import By


class MainPageLocators():
    pass



class LoginPageLocators():
    USER_NAME = (By.CSS_SELECTOR, "input[placeholder='Enter Username']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Enter Password']")
    PASSWORD_ONE_TIME = (By.CSS_SELECTOR, "input[placeholder='One-time password']")
    CHECKBOX_ONE_TIME_PASSWORD = (By.CSS_SELECTOR, "label[for = 'isSupport']")
    SIGN_IN_BUTTON = (By.CLASS_NAME, "login_buton")
    ADVANCED_BUTTON = (By.ID, "details-button")
    PROCEED_TO_PORTAL_BUTTON = (By.ID, "proceed-link")
    ERROR_IN_CONSOLE = (By.CSS_SELECTOR, '.console-error-class')

class DashboardPageLocators():
    pass


class BasePageLocators():
    USER_NAME = (By.CSS_SELECTOR, ".admin_title")