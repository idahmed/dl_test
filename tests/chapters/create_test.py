from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

def login(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL + "/login/")
    assert page.title() == "Login"
    page.close()
    

def test_chapters_create(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(BASE_URL + "/chapters/create/")
    assert page.locator('h2:has-text("Chapters")').is_visible()
    page.close()