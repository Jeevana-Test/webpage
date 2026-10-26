from pages.base_page import BasePage
from config.settings import BASE_URL
from playwright.sync_api import Page
from config.logger import logger
login_detail=["testuser","testpassword"]


def test_login_page(page: Page):
    logger.info("Starting test_login_page")

    login_page = BasePage(page)
    login_page.navigate(BASE_URL)

    assert login_page.is_visible("#login-button"), \
        "Login button is not visible"

    logger.info("Login page loaded successfully")
def test_invalid_login(page):
    logger.info("Starting invalid login test")

    login_page = BasePage(page)

    login_page.navigate(BASE_URL)
    login_page.fill("#user-name", "invalid_user")
    login_page.fill("#password", "invalid_pass")
    login_page.click("#login-button")

    page.wait_for_selector("[data-test='error']")

    assert login_page.is_visible("[data-test='error']")

    logger.info("Invalid login error displayed successfully")


def test_login_empty_credentials(page: Page):
    logger.info("Starting empty credentials test")

    login_page = BasePage(page)

    try:
        login_page.navigate(BASE_URL)

        login_page.fill("#user-name", "")
        login_page.fill("#password", "")
        login_page.click("#login-button")

        page.wait_for_selector("[data-test='error']")

        error_message = page.locator(
            "[data-test='error']"
        ).text_content()

        logger.info(f"Error Message: {error_message}")

        assert login_page.is_visible("[data-test='error']")

        logger.info("Empty credentials validation passed")

    except Exception as e:
        logger.error(f"Empty credentials test failed: {str(e)}")

        page.screenshot(
            path="screenshots/empty_credentials_failure.png"
        )

        raise
