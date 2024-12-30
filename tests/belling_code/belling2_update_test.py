from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_belling_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "billing_codes/")
    
    # Locate the row in the table containing the text 'Test_belling1'
    row = page.locator('tr', has_text="Test_belling1")
    assert row.count() > 0, "The row containing 'Test_belling1' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_belling1' is not visible."
    button.click()

    # Update tube information 
    page.fill("#title", "Test_belling1_update")
    assert page.locator('#title').get_attribute('required') is not None, "The 'title' field is not marked as required."
    page.fill("#nomenclature", "nomenclature1")
    page.locator('#key').select_option("DH")
    page.fill("#coefficient", "60")
    page.fill("#status", "active")
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "billing_codes/")
    assert page.locator('h2:has-text("Belling configurations")').is_visible(), "'Belling configurations' header is not visible"
