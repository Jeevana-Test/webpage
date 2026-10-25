# File: tests/test_products.py

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.settings import USERS
from playwright.sync_api import Page

def test_products_list_visible(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # Login first
    login_page.navigate_to_login_page()
    login_page.login(USERS["valid_user"]["email"], USERS["valid_user"]["password"])

    # Verify product list is visible
    assert products_page.is_product_list_visible(), "Product list is not visible"

def test_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # Login first
    login_page.navigate_to_login_page()
    login_page.login(USERS["valid_user"]["email"], USERS["valid_user"]["password"])

    # Add product to cart
    products_page.add_first_product_to_cart()
    assert products_page.is_cart_badge_visible(), "Cart badge is not visible after adding a product"