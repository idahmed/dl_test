from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")



def test_chapter_create_page(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "chapters")
    assert page.url == f"{BASE_URL}chapters/"
    add_button = page.locator("a.btn.btn-primary:has-text('Add')")
    assert add_button.is_visible()
    assert add_button.get_attribute("href") == "/chapters/create/"
    add_button.click()
    assert page.url == f"{BASE_URL}chapters/create/"
    page.fill("#code", "Test Chapter")
    page.fill("#name", "Test Chapter")
    page.click("button:has-text('Save')")
    assert page.url == f"{BASE_URL}chapters/"
    assert page.locator("div.alert.alert-success").is_visible()
    
    