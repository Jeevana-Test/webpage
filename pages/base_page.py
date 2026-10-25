from playwright.sync_api import Page
from config.settings import TIMEOUT
from config.settings import BASE_URL

class BasePage:
    def __init__(self,page:Page):
        self.page=page
        self.timeout=TIMEOUT
        self.base_url=BASE_URL

    def navigate(self,url):
        self.page.goto(url,timeout=60000)
        self.page.wait_for_load_state("domcontentloaded")

    def click(self,locator):
        self.page.locator(locator).click()

    def fill(self,locator,text):
        self.page.locator(locator).fill(text)

    def is_visible(self,locator):
        return self.page.locator(locator).is_visible()

    def get_text(self,locator):
        return self.page.locator(locator).inner_text()
