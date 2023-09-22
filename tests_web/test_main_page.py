from pages.locators import MainPageLocators
from pages.login_page import LoginPage
import time


def test_buttons_appears(browser, get_url_web):
    page = LoginPage(browser, get_url_web)
    page.open()
    page.enter_with_valid_creds()
    page.wait_element_presented(*MainPageLocators.CALLS_BUTTON)
    time.sleep(5)
