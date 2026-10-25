# File: pages/products_page.py

from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    product_item = ".inventory_item"
    add_to_cart_button = ".btn_inventory"
    cart_badge = ".shopping_cart_badge"

    def is_product_list_visible(self):
        return self.is_visible(self.product_item)

    def add_first_product_to_cart(self):
        self.click(self.add_to_cart_button)

    def is_cart_badge_visible(self):
        return self.is_visible(self.cart_badge)