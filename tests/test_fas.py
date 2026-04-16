from playwright.sync_api import Page, expect
from playwright.sync_api import BrowserContext

def test_opened(page:Page, base_url):
    page.goto(f"{base_url}/login.html")
    expect(page.get_by_text('Login to FashionHub')).to_be_visible()

def test_logged_in(page:Page, base_url):
    page.goto(f"{base_url}/login.html")
    page.locator('#username').fill('demouser')
    page.locator('#password').fill('fashion123')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_text('Welcome, demouser!')).to_be_visible()

