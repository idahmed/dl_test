import re
from playwright.sync_api import Playwright, sync_playwright, expect

def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("http://localhost:8000/login/")
    page.get_by_label("Email:").fill("admin@admin.com")
    page.get_by_label("Password:").fill("admin")
    page.get_by_role("button", name="Login").click()
    
    page.wait_for_timeout(timeout=5 * 1000)


def chapters_update(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("http://localhost:8000/login/")
    page.get_by_label("Email:").fill("admin@admin.com")
    page.get_by_label("Password:").fill("admin")
    page.get_by_role("button", name="Login").click()


    page.goto("http://localhost:8000/chapters/")
    
    # Find and click on the chapter to modify
    page.get_by_role("row", name="TS1 TEST1 TEST TEST").get_by_role("link").nth(1).click()
    
    # Try using a more specific selector
    code_input = page.get_by_placeholder("Code", exact=True)
    page.wait_for_timeout(3000)  

    # Check if the "Code" input is available
    if code_input.is_visible():
        print("Code input field found!")
    else:
        print("Code input field not found!")

    # chapter update
    code_input.fill("TS1_MODIFIED")  # Fill the Code field
    page.get_by_placeholder("name", exact=True).fill("TEST1_MODIFIED")
    page.get_by_placeholder("loinc code", exact=True).fill("SS123_MODIFIED")
    page.get_by_placeholder("comment", exact=True).fill("MODIFIED COMMENT")
    page.get_by_placeholder("comment_placement", exact=True).fill("MODIFIED COMMENT")
    page.get_by_label("Print name:").check()
    page.get_by_role("button", name="Enregistrer").click()

    page.wait_for_timeout(2000) 

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    chapters_update(playwright)