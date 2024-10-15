import re
from playwright.sync_api import Playwright, sync_playwright, expect

def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    
    # Login
    page.goto("http://localhost:8000/login/")
    page.get_by_label("Email:").fill("admin@admin.com")
    page.get_by_label("Password:").fill("admin")
    page.get_by_role("button", name="Login").click()

    page.wait_for_timeout(5000)  
    return page  


def chapters_delete(playwright: Playwright) -> None:
    # Login
    page = login(playwright)

    page.goto("http://localhost:8000/chapters/")
    page.wait_for_timeout(2000) 

    # Assuming the button is in the same row that contains "TS1_MODIFIED"
    row = page.locator('tr', has_text="TS1_MODIFIED")
    delete_button = row.locator('a[data-bs-toggle="modal"]').click() 


    # Wait for the modal to appear and click confirm within the modal
    page.wait_for_selector('div.modal.show')  
    page.get_by_role("button", name="Supprimer").click() 

    page.wait_for_timeout(2000)  

    # ---------------------
    context = page.context
    context.close()
    browser = context.browser
    browser.close()


with sync_playwright() as playwright:
    chapters_delete(playwright)