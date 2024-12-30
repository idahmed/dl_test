from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_tube_update(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "tubeconfig/")
    
    # Locate the row in the table containing the text 'Test_Tube1'
    row = page.locator('tr', has_text="Test_Tube1")
    assert row.count() > 0, "The row containing 'Test_Tube1' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_Tube1' is not visible."
    button.click()

    # Update tube information 
    page.fill("#name", "Test_Tube1_update")
    name_is_required = page.locator('#name').get_attribute('required')
    assert name_is_required is not None, "The 'name' field is not marked as required."
    page.fill("#quantity", "5")
    page.locator("#unit").select_option("unit") 
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "tubeconfig/")
    assert page.locator('h2:has-text("Tubes")').is_visible(), "The tubes page could not be loaded."
