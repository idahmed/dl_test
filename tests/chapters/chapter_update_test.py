from playwright.sync_api import sync_playwright
import pytest
import os

BASE_URL = os.getenv("BASE_URL")

def test_chapter_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed."
    page.goto(BASE_URL + "chapters/")
    assert page.locator('h2:has-text("Chapters")').is_visible(), "The list of chapters is not visible."
    
    # Locate the chapter to update
    chapter_row = page.get_by_role("row", name="Test_Chapter2 Test_Chapter2")
    assert chapter_row.is_visible(), "The chapter 'Test_Chapter2' is not visible in the list."
    chapter_row.get_by_role("link").nth(1).click()
    
    # Update the chapter
    page.fill("#code", "Chapter_updateTest")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Chapter_updateTest")
    name_is_required = page.locator('#name').get_attribute('required')
    assert name_is_required is not None, "The 'name' field is not marked as required."
    page.click("button:has-text('Save')")
    
    # Verify the update
    page.goto(BASE_URL + "chapters/")
    assert page.locator('h2:has-text("Chapters")').is_visible(), "The list of chapters is not visible after the update."
