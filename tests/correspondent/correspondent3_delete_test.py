from playwright.sync_api import sync_playwright
import pytest
import os

BASE_URL = os.getenv("BASE_URL")

def test_correspondent_delete(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed"
    
    page.goto(BASE_URL + "correspondents/")
    row = page.locator('tr', has_text="Test_correspondent1_update")
    assert row.is_visible(), "The row containing text 'Test_correspondent1_update' is not found"
    delete_button = row.locator('a[data-bs-toggle="modal"]')
    assert delete_button.is_visible(), "Delete button in the row is not found"
    delete_button.click()

    # Verify that the modal is displayed
    modal = page.locator('div.modal.show')
    print(modal.get_attribute("class"))
    assert modal.is_visible(), "The confirmation modal did not appear"

    # Verify that the delete button in the modal is visible
    delete_button_in_modal = modal.locator("button:has-text('Delete')")
    assert delete_button_in_modal.is_visible(), "'Delete' button in the modal is not found"

    delete_button_in_modal.click()
    assert not modal.is_visible(), "The deletion modal is still visible after clicking delete"
    assert page.locator('h2:has-text("List of correspondent")').is_visible(), "'List of correspondent' header is not visible"

