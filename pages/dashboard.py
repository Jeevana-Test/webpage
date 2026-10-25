from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    inventory_items = ".inventory_item"
    cart_button = "#shopping_cart_container"
    menu_button = "#react-burger-menu-btn"
    logout_button = "#logout_sidebar_link"

    def is_inventory_visible(self):
        return self.is_visible(self.inventory_items)

    def click_cart_button(self):
        self.click(self.cart_button)

    def open_menu(self):
        self.click(self.menu_button)

    def logout(self):
        self.open_menu()
        self.click(self.logout_button)