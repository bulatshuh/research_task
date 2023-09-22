from .base_page import BasePage
from .locators import LoginPageLocators
from data import TestData


class LoginPage(BasePage):
    def enter_with_valid_creds(self):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(TestData.phone_number)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()
        self.browser.find_element(*LoginPageLocators.USE_PASSWORD_BUTTON).click()
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(TestData.password)
        self.browser.find_element(*LoginPageLocators.CONTINUE_BUTTON).click()
        