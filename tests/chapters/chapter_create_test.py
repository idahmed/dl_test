from playwright.sync_api import sync_playwright
import pytest
import os

BASE_URL = os.getenv("BASE_URL")

def test_chapter_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed."
    page.goto(BASE_URL + "chapters/create")
    page.fill("#code", "Test_Chapter1")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Test_Chapter1")
    name_is_required = page.locator('#name').get_attribute('required')
    assert name_is_required is not None, "The 'name' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "chapters/")
    assert page.locator('h2:has-text("Chapters")').is_visible(), "The list of chapters is not visible."

def test_chapter_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed."
    page.goto(BASE_URL + "chapters/create")
    page.fill("#code", "Test_Chapter2")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Test_Chapter2")
    name_is_required = page.locator('#name').get_attribute('required')
    assert name_is_required is not None, "The 'name' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "chapters/")
    assert page.locator('h2:has-text("Chapters")').is_visible(), "The list of chapters is not visible."
