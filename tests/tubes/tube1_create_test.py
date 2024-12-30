from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


def test_tube_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the insurance creation page
    page.goto(BASE_URL + "tubeconfig/create/")
    page.fill("#name", "Test_Tube1")
    assert page.locator('#name').get_attribute('required') is not None, "The 'name' field is not marked as required."
    page.fill("#quantity", "20")
    page.locator('#unit').select_option("ml")
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "tubeconfig/")
    assert page.locator('h2:has-text("Tubes")').is_visible(), "The tube list page did not load."


def test_tube_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the insurance creation page
    page.goto(BASE_URL + "tubeconfig/create/")
    page.fill("#name", "TTest_Tube2")
    assert page.locator('#name').get_attribute('required') is not None, "The 'name' field is not marked as required."
    page.fill("#quantity", "10")
    page.locator('#unit').select_option("unit")
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "tubeconfig/")
    assert page.locator('h2:has-text("Tubes")').is_visible(), "The tube list page did not load."
