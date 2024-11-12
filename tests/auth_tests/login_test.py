from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


def test_login_page(page):
    page.goto(BASE_URL + "login/")
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    

def test_login_with_invalid_credentials(page):
    page.goto(BASE_URL + "login/")
    assert page.title() == "Login"
    page.fill("#email", "admin@nonadmin.com")
    page.fill("#password", "nonadmin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}login/"
    