from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")
def test_correspondent_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "correspondents/create/")
    page.locator("#type").select_option("Lab")  
    page.fill("#code", "Test_correspondent1")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "correspondents/")
    assert page.locator('h2:has-text("List of correspondent")').is_visible()
    
    
def test_correspondent_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "correspondents/create/")
    page.locator("#type").select_option("Hospital")  
    page.fill("#code", "Test_correspondent2")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "correspondents/")
    assert page.locator('h2:has-text("List of correspondent")').is_visible()