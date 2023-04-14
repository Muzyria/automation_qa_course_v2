from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """form fields"""
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, 'p[id="name"]')  # '#output #name'
    CREATED_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')


class CheckBoxPageLocators:
    """checkbox"""
    EXPEND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Collapse all"]')

    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ('.//ancestor::span[@class="rct-text"]')

