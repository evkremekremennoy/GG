import time

from .pages.dashboard_page import MainPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.skip
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        pass

#@pytest.mark.login_page
class TestLoginPage():
    def test_guest_should_can_see_login_page(self, browser):
        link = "https://portal.galaxygaming.net/"
        page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_in_portal()  # выполняем метод страницы — переходим на страницу логина

