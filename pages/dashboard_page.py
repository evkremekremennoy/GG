from .base_page import BasePage
from .locators import DashboardPageLocators


class DashboardPage(BasePage):
    def should_be_open_user_management_page(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.USERS_GRAF).click()
        assert "listusers" in self.browser.current_url, "link from dashboard to UserManagement doesn't work"

    def should_be_open_adduser_page(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.ADDUSERS_LINK).click()
        assert "addUser/fromDashboard" in self.browser.current_url, "link from dashboard to ADD USER doesn't work"

    def should_be_open_table_page(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.TABLES_GRAF).click()
        assert "listgametables" in self.browser.current_url, "link from dashboard to Tables doesn't work"

    def should_be_open_award_report_page_by_link_last_10_jackpots_won(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.LAST_10_JACKPOTS_GRAF).click()
        assert "awardreport/2023-09-13T00:00:00/2023-08-29T00:00:00" in self.browser.current_url, "link from " \
                                                                                                  "dashboard to Award reports doesn't work"

    def should_be_open_activity_report_page(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.ACTIVITY_REPORT_GRAF).click()
        assert "activityreport" in self.browser.current_url, "link from dashboard to Activity Reports doesn't work"

    def should_be_open_jackpot_page(self):
        self.autorithation_user()
        self.browser.find_element(*DashboardPageLocators.JACKPOTS_GRAF).click()
        assert "listjackpots" in self.browser.current_url, "link from dashboard to Jackpot doesn't work"
