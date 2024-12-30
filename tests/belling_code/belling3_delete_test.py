from playwright.sync_api import sync_playwright
import pytest
import os

BASE_URL = os.getenv("BASE_URL")

def test_belling_delete1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed"
    page.goto(BASE_URL + "billing_codes/")
    row = page.locator('tr', has_text="Test_belling2")
    assert row.is_visible(), "The row containing text 'Test_belling2' is not found"
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
    assert page.locator('h2:has-text("Belling configurations")').is_visible(), "'Belling configurations' header is not visible"
    
    
def test_belling_delete2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}", "Redirection after login failed"
    page.goto(BASE_URL + "billing_codes/")
    row = page.locator('tr', has_text="Test_belling1_update")
    assert row.is_visible(), "The row containing text 'Test_belling1_update' is not found"
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
    assert page.locator('h2:has-text("Belling configurations")').is_visible(), "'Belling configurations' header is not visible"

