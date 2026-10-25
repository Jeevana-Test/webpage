# File: pages/products_page.py

from pages.base_page import BasePage

class ProductsPage(BasePage):
    product_item = ".inventory_item"
    first_add_to_cart_button = ".btn_inventory"
    def __init__(self, page):
        super().__init__(page)
    product_list = ".inventory_item"
    add_to_cart_button = ".btn_inventory"
    cart_badge = ".shopping_cart_badge"

    def is_product_list_visible(self):
        print("URL:", self.page.url)
        print("Items:", self.page.locator(".inventory_item").count())
        return self.page.locator(".inventory_item").count() > 0

    def add_first_product_to_cart(self):
        self.page.locator(self.first_add_to_cart_button).first.click()

    def is_cart_badge_visible(self):
        return self.is_visible(self.cart_badge)

