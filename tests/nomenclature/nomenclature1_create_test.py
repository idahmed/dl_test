from playwright.sync_api import sync_playwright
import pytest
import os
from datetime import datetime, timedelta
BASE_URL = os.getenv("BASE_URL")
def test_nomenclature_create_page1(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/create/")
    page.fill("#code", "Test_nomenclature1")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#label", "Test1")
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    page.locator("#coefficient_key").select_option("HN")  
    page.fill("#coefficient", "200")
    # Set valid dates: application_date today +5 days
    application_date = (datetime.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    suspension_date = (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d")
    # Verify 'application_date' is required
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    
    # Fill in the dates and save
    page.fill('#application_date', application_date)
    page.fill('#suspension_date', suspension_date)
    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "nomenclatures/")
    assert page.locator('h2:has-text("Nomenclatures")').is_visible()
    
    
def test_nomenclature_create_page2(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/create/")
    page.fill("#code", "Test_nomenclature1")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#label", "Test2")
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    page.locator("#coefficient_key").select_option("DH")  
    page.fill("#coefficient", "300")
    # Set valid dates: application_date today + 15 days and suspension_date 25 days after application_date
    application_date = (datetime.today() + timedelta(days=15)).strftime("%Y-%m-%d")
    suspension_date = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
    
    # Verify 'application_date' is required
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    
    # Fill in the dates and save
    page.fill('#application_date', application_date)
    page.fill('#suspension_date', suspension_date)

    page.click("button:has-text('Save')")
    page.goto(BASE_URL + "nomenclatures/")
    assert page.locator('h2:has-text("Nomenclatures")').is_visible()
    
    
def test_nomenclature_create_page3(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/create/")
    page.fill("#code", "Test_nomenclature2")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#label", "Test2")
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    page.locator("#coefficient_key").select_option("HN")  
    page.fill("#coefficient", "200")
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
    assert page.locator('h2:has-text("Add new Nomenclature")').is_visible()
    
    
def test_nomenclature_create_page4(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    
    #  Verify that duplicate nomenclature for the same date range are not allowed.
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "nomenclatures/create/")
    page.fill("#code", "Test_nomenclature3")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None, "The 'code' field is not marked as required."
    page.fill("#label", "Test3")
    label_is_required = page.locator('#label').get_attribute('required')
    assert label_is_required is not None, "The 'label' field is not marked as required."
    page.locator("#coefficient_key").select_option("HN")  
    page.fill("#coefficient", "200")
    # Set valid dates: application_date today + 13 days and suspension_date 2 days after application_date
    application_date = (datetime.today() + timedelta(days=12)).strftime("%Y-%m-%d")
    suspension_date = (datetime.today() + timedelta(days=5)).strftime("%Y-%m-%d")
    
    # Verify 'application_date' is required
    application_date_is_required = page.locator('#application_date').get_attribute('required')
    assert application_date_is_required is not None, "The 'application_date' field is not marked as required."
    
    # Fill in the dates and save
    page.fill('#application_date', application_date)
    page.fill('#suspension_date', suspension_date)
    page.click("button:has-text('Save')")
    assert page.locator('h2:has-text("Add new Nomenclature")').is_visible()
    
    

