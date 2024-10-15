from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

def test_login_page(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL + "login/")
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.close()
    

def test_login_with_invalid_credentials(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL + "login/")
    assert page.title() == "Login"
    page.fill("#email", "admin@nonadmin.com")
    page.fill("#password", "nonadmin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}login/"
    page.close()
