from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")
def test_liquid_code_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "liquides_codes/")

    # Locate the row in the table containing the text '01'
    row = page.locator('tr', has_text="01")
    assert row.count() > 0, "The row containing '01' does not exist."
    page.click("button:has-text('Edit')")
    
    # Update the code
    page.locator('input[value="Code 1"]').fill("Code 1_Test")
    page.click("button:has-text('Save')")
    
    # Wait for the update to reflect
    row = page.locator('tr', has_text="01")
    row.locator('span.title-display:has-text("Code 1_Test")').wait_for(state="visible", timeout=5000)
    assert row.locator('span.title-display:has-text("Code 1_Test")').is_visible(), "The updated code 'Code 1_Test' does not appear in the table."
    
def test_liquid_code_update2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "liquides_codes/")

    # Locate the row in the table containing the text '01'
    row = page.locator('tr', has_text="01")
    assert row.count() > 0, "The row containing '01' does not exist."
    page.click("button:has-text('Edit')")
    
    # Update the code
    page.locator('input[value="Code 1_Test"]').fill("Code 1")
    page.click("button:has-text('Save')")
    
    # Wait for the update to reflect
    row = page.locator('tr', has_text="01")
    row.locator('span.title-display:has-text("Code 1")').wait_for(state="visible", timeout=5000)
    assert row.locator('span.title-display:has-text("Code 1")').is_visible(), "The updated code 'Code 1' does not appear in the table."
