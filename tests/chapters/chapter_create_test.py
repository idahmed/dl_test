from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")



def test_chapter_create_page(page):
    page.goto(BASE_URL + "login/")
    page.locator("#djHideToolBarButton").click()
    assert page.title() == "Login"
    page.fill("#email", "admin@admin.com")
    page.fill("#password", "admin")
    page.click("button:has-text('Login')")
    assert page.url == f"{BASE_URL}"
    page.goto(BASE_URL + "chapters/create")
    code_is_required = page.locator('#code').get_attribute('required')
    assert code_is_required is not None

    comment_is_required = page.locator('#comment_placement').get_attribute('required')
    assert comment_is_required is None

    






    # assert page.url == f"{BASE_URL}chapters/"
    # add_button = page.locator("a.btn.btn-primary:has-text('Add')")
    # page.screenshot('fullpage-screenshot.png');
    # assert add_button.is_visible()
    # assert add_button.get_attribute("href") == "/chapters/create/"
    # add_button.click()
    # assert page.url == f"{BASE_URL}chapters/create/"
    # page.fill("#code", "Test Chapter")

    # page.click("button:has-text('Save')")

    # assert add_button.get_attribute("href") == "/chapters/create/"


    # page.fill("#name", "Test Chapter")
    # assert page.url == f"{BASE_URL}chapters/"
    # assert page.locator("div.alert.alert-success").is_visible()

    # page.goto
    
    