from playwright.sync_api import sync_playwright
import pytest
import os
from datetime import datetime, timedelta
BASE_URL = os.getenv("BASE_URL")
def test_nomenclature_update_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/")
    
    # Locate the row in the table containing the text 'Test_nomen'
    row = page.locator('tr', has_text="Test_nomen Test1")
    assert row.count() > 0, "The row containing 'Test_nomen' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_nomen' is not visible."
    button.click()
    
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    page.locator("#coefficient_key").select_option("DH")  
    page.fill("#coefficient", "400")
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "nomenclatures/")
    assert page.locator('h2:has-text("Nomenclatures")').is_visible()
    
    
def test_nomenclature_update_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/")
    
    # Locate the row in the table containing the text 'Test_nomen'
    row = page.locator('tr', has_text="Test_nomen Test1")
    assert row.count() > 0, "The row containing 'Test_nomen' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_nomen' is not visible."
    button.click()
    
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    # Verify that 'application_date' cannot be after 'suspension_date'.
    suspension_date = (datetime.today() + timedelta(days=11)).strftime("%Y-%m-%d")
    application_date= (datetime.today() + timedelta(days=21)).strftime("%Y-%m-%d")
    
    #Verify 'application_date' is required
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    
    # Fill in the dates and save
    page.fill('#application_date', application_date)
    page.fill('#suspension_date', suspension_date)
    page.click("button:has-text('Save')")
    assert page.locator('h2:has-text("nomenclature update")').is_visible()
    
    
def test_nomenclature_update_page3(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/")
    
    # Locate the row in the table containing the text 'Test_nomen'
    row = page.locator('tr', has_text="Test_nomen Test1")
    assert row.count() > 0, "The row containing 'Test_nomen' does not exist."
    button = row.locator('a.btn.btn-warning.btn-sm')
    assert button.is_visible(), "The edit button for 'Test_nomen' is not visible."
    button.click()
    
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    #  Verify that duplicate nomenclature for the same date range are not allowed.
    application_date3 = (datetime.today() + timedelta(days=20)).strftime("%Y-%m-%d")
    suspension_date3 = (datetime.today() + timedelta(days=22)).strftime("%Y-%m-%d")
    
    # Verify 'application_date' is required
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    
    # Fill in the dates and save
    page.fill('#application_date', application_date3)
    page.fill('#suspension_date', suspension_date3)
    page.click("button:has-text('Save')")
    assert page.locator('h2:has-text("nomenclature update")').is_visible()
    
    
