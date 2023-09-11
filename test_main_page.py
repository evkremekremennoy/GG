import time

from .pages.dashboard_page import MainPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.skip
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        pass

#@pytest.mark.login_page
@pytest.mark.skip
class TestLoginPage():
    #@pytest.mark.skip
    def test_user_should_can_log_in(self, browser):
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_in_portal()  # выполняем метод страницы — переходим на страницу логина
    #@pytest.mark.skip
    def test_user_should_not_login_with_wrong_password(self, browser):
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_fail_with_wrong_password()  # выполняем метод страницы — переходим на страницу логина
        page.should_not_be_user_name_in_header()
    #@pytest.mark.skip
    def test_user_should_not_loging_with_wrong_username(self, browser):
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_fail_with_wrong_username()  # выполняем метод страницы — переходим на страницу логина
        page.should_not_be_user_name_in_header()

    def test_user_can_input_one_time_password(self, browser):
        #check work of 'Connect with support user one-time password' checkbox
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_change_password_to_One_time_password()
    #@pytest.mark.skip
    def test_user_cannt_use_regular_password_like_one_time_password(self, browser):
        #check work of 'Connect with support user one-time password' checkbox
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser, link)
        page.open()
        page.should_fail_using_passwor_in_one_time_password_field()