from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")


def test_insurance_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the insurance creation page
    page.goto(BASE_URL + "insurance/create/")
    page.fill("#code", "Test_insurance1")
    assert page.locator('#code').get_attribute('required') is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Test_insurance1")
    page.locator('#type').select_option("caisse")
    assert page.locator('#type').get_attribute('required') is not None, "The 'type' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "insurance/")
    assert page.locator('h2:has-text("Insurance")').is_visible(), "The insurance list page did not load."


def test_insurance_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login", "The login page did not load correctly."
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Login failed or incorrect redirect after login."
    
    # Navigate to the insurance creation page
    page.goto(BASE_URL + "insurance/create/")
    page.fill("#code", "Test_insurance2")
    assert page.locator('#code').get_attribute('required') is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Test_insurance2")
    page.locator('#type').select_option("mutual")
    assert page.locator('#type').get_attribute('required') is not None, "The 'type' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "insurance/")
    assert page.locator('h2:has-text("Insurance")').is_visible(), "The insurance list page did not load."
