from playwright.sync_api import Playwright, sync_playwright, expect
import pytest, time


@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()

def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="Создать первый сценарий playwright").get_by_role("checkbox").check()
    page.get_by_role("link", name="Active").click()
    time.sleep(5)

