from playwright.sync_api import sync_playwright
import pytest
import os
BASE_URL = os.getenv("BASE_URL")

def test_chapters_create(page):
    page.goto(BASE_URL + "/chapters/create/")
    assert page.locator('h2:has-text("Chapters")').is_visible()

def test_login(page):
    page.goto(BASE_URL + "/login/")
    assert page.title() == "Login"