# File: tests/test_dashboard.py

from pages.dashboard import DashboardPage
from pages.login_page import LoginPage
from config.settings import BASE_URL, USERS
from playwright.sync_api import Page

def test_dashboard_inventory_visible(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Login first
    login_page.navigate_to_login_page()
    login_page.login(USERS["valid_user"]["email"], USERS["valid_user"]["password"])

    # Verify inventory items are visible
    assert dashboard_page.is_inventory_visible(), "Inventory items are not visible on the dashboard"

def test_dashboard_cart_navigation(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Login first
    login_page.navigate_to_login_page()
    login_page.login(USERS["valid_user"]["email"], USERS["valid_user"]["password"])

    # Navigate to cart
    dashboard_page.click_cart_button()
    assert page.url.endswith("/cart.html"), "Failed to navigate to the cart page"

def test_dashboard_logout(page: Page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Login first
    login_page.navigate_to_login_page()
    login_page.login(USERS["valid_user"]["email"], USERS["valid_user"]["password"])

    # Logout
    dashboard_page.logout()
    assert page.url == BASE_URL, "Logout did not redirect to the login page"