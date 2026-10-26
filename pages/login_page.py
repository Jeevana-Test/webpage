from playwright.sync_api import Page
from pages.base_page import BasePage
from config.settings import BASE_URL

class LoginPage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
    User_name="#user-name"
    Password="#password"
    login_button="#login-button"
    error_message=".error-message-container"


    def navigate_to_login_page(self):
        self.navigate(self.base_url)

    def login(self,username,password):
        self.fill(self.User_name,username)
        self.fill(self.Password,password)
        self.click(self.login_button)

    def is_error_message_visible(self):
        return self.is_visible(self.error_message)

    def is_login_button_visible(self):
        return self.is_visible(self.login_button)