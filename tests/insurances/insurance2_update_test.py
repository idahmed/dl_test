from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_insurance_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "insurance/")
    
    # Locate the row in the table containing the text 'Test_insurance1'
    row = page.locator('tr', has_text="Test_insurance1")
    assert row.count() > 0, "The row containing 'Test_insurance1' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'TTest_insurance1' is not visible."
    button.click()

    # Update tube information 
    page.fill("#code", "Test_insurance1_update")
    assert page.locator('#code').get_attribute('required') is not None, "The 'code' field is not marked as required."
    page.fill("#name", "Test_insurance1_update")
    page.locator('#type').select_option("mutual")
    assert page.locator('#type').get_attribute('required') is not None, "The 'type' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "insurance/")
    assert page.locator('h2:has-text("Insurance")').is_visible(), "The insurance list page did not load."
