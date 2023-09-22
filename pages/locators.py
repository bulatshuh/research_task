from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '.VkIdForm__input')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[type="submit"] .FlatButton__in')
    USE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.vkc__Bottom__switchToPassword')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.vkc__Password__Wrapper .vkc__TextField__input')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.vkuiButton__in')


class MainPageLocators:
    CALLS_BUTTON = (By.CSS_SELECTOR, '.LeftMenuOld-module__container--G1UQ7 :nth-child(4)')
    MESSAGES_BUTTON = (By.CSS_SELECTOR, '')
