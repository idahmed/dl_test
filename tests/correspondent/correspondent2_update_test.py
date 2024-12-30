from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_correspondent_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "correspondents/")
    
    # Locate the row in the table containing the text 'Test_correspondent1'
    row = page.locator('tr', has_text="Test_correspondent1")
    assert row.count() > 0, "The row containing 'Test_correspondent1' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_correspondent1' is not visible."
    button.click()

    # Update tube information 
    page.locator("#type").select_option("Clinic")  
    page.fill("#code", "Test_correspondent1_update")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "correspondents/")
    assert page.locator('h2:has-text("List of correspondent")').is_visible()
