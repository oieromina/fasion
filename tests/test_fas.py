from asyncio import wait_for

from playwright.sync_api import Page, expect



def test_opened(page:Page, base_url):
    page.goto(f"{base_url}/login.html")
    expect(page.get_by_text('Home')).to_be_visible()

def test_logged_in(page:Page, base_url, user_email, password):
    page.goto(f"{base_url}/login.html")
    page.get_by_role(role='button', name='Consent').click()
    page.get_by_role(role='link', name=' Signup / Login').click()
    expect(page.get_by_role(role='button', name='Login')).to_be_visible()
    page.locator('input[data-qa="login-email"]').fill(user_email)
    page.locator('input[data-qa="login-password"]').fill(password)
    page.get_by_role(role='button', name='Login').click()
    expect(page.get_by_role(role='heading', name='CATEGORY')).to_be_visible()


