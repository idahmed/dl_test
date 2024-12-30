from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_tube_archive1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "tubeconfig/")
    
    # Locate the row in the table containing the text 'Test_Tube2'
    row = page.locator('tr', has_text="Test_Tube2")
    assert row.count() > 0, "The row containing 'Test_Tube2' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_Tube2' is not visible."
    button.click()

    page.click("button:has-text('Archive')")
    # Verify that the modal is displayed
    modal = page.locator('div.modal.show')
    print(modal.get_attribute("class"))
    assert modal.is_visible(), "The confirmation modal did not appear"

    # Verify that the archive button in the modal is visible
    archive_button_in_modal = modal.locator("button:has-text('Archive')")
    assert archive_button_in_modal.is_visible(), "'Archive' button in the modal is not found"
    archive_button_in_modal.click()
    assert page.locator('h2:has-text("update")').is_visible(), "The tubes page could not be loaded."
    
    
    
def test_tube_archive2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "tubeconfig/")
    row = page.locator('tr', has_text="Test_Tube1_update")
    assert row.count() > 0, "The row containing 'Test_Tube1_update' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_Tube1_update' is not visible."
    button.click()

    page.click("button:has-text('Archive')")
    modal = page.locator('div.modal.show')
    print(modal.get_attribute("class"))
    assert modal.is_visible(), "The confirmation modal did not appear"
    archive_button_in_modal = modal.locator("button:has-text('Archive')")
    assert archive_button_in_modal.is_visible(), "'Archive' button in the modal is not found"
    archive_button_in_modal.click()
    assert page.locator('h2:has-text("update")').is_visible(), "The tubes page could not be loaded."
