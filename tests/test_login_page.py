from pages.base_page import BasePage
from config.settings import BASE_URL
from playwright.sync_api import Page
login_detail=["testuser","testpassword"]

def test_login_page(page:Page):
    login_page=BasePage(page)
    login_page.navigate(BASE_URL)
    assert login_page.is_visible("#login-button"), "Login button is not visible"

def test_invalid_login(page):
    login_page = BasePage(page)

    login_page.navigate(BASE_URL)
    login_page.fill("#user-name", "invalid_user")
    login_page.fill("#password", "invalid_pass")
    login_page.click("#login-button")

    page.wait_for_selector("[data-test='error']")

    assert login_page.is_visible("[data-test='error']")



def test_login_empty_credentials(page: Page):
    login_page = BasePage(page)

    # Navigate to the login page
    login_page.navigate(BASE_URL)

    # Attempt to login with empty credentials
    login_page.fill("#user-name", "")
    login_page.fill("#password", "")
    login_page.click("#login-button")

    # Verify error message is displayed
    page.wait_for_selector("[data-test='error']")
    error_message = page.locator("[data-test='error']").text_content()
    print(f"Error message for empty credentials: {error_message}")
    assert login_page.is_visible("[data-test='error']")