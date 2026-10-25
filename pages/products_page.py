# File: pages/products_page.py

from pages.base_page import BasePage

class ProductsPage(BasePage):
    first_add_to_cart_button = "(//button[contains(@class, 'btn_inventory')])[1]"  # XPath for the first button
    def __init__(self, page):
        super().__init__(page)
    product_list = ".inventory_item"
    add_to_cart_button = ".btn_inventory"
    cart_badge = ".shopping_cart_badge"

    def is_product_list_visible(self):
        return self.is_visible(self.product_list)

    def add_first_product_to_cart(self):
        self.click(self.first_add_to_cart_button)

    def is_cart_badge_visible(self):
        return self.is_visible(self.cart_badge)