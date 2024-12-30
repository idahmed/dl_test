from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


def test_belling_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the belling creation page
    page.goto(BASE_URL + "billing_codes/create/")
    page.fill("#title", "Test_belling1")
    assert page.locator('#title').get_attribute('required') is not None, "The 'title' field is not marked as required."
    page.fill("#nomenclature", "nomenclature1")
    page.locator('#key').select_option("B")
    page.fill("#coefficient", "50")
    page.fill("#status", "active")
    page.locator("#modifiable").check()
    page.locator("#active").check()
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "billing_codes/")
    assert page.locator('h2:has-text("Belling configurations")').is_visible(), "The belling list page did not load."



def test_belling_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the belling creation page
    page.goto(BASE_URL + "billing_codes/create/")
    page.fill("#title", "Test_belling2")
    assert page.locator('#title').get_attribute('required') is not None, "The 'title' field is not marked as required."
    page.fill("#nomenclature", "nomenclature1")
    page.locator('#key').select_option("HN")
    page.fill("#coefficient", "30")
    page.fill("#status", "active")
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "billing_codes/")
    assert page.locator('h2:has-text("Belling configurations")').is_visible(), "The belling list page did not load."

