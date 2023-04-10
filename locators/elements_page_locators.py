from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """form fields"""
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userName"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'input[id="userName"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'input[id="userName"]')
    SUBMIT = (By.CSS_SELECTOR, 'input[id="userName"]')

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    CREATED_EMAIL = (By.CSS_SELECTOR, 'input[id="userName"]')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'input[id="userName"]')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'input[id="userName"]')
