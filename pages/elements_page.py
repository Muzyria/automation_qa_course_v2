import time

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('qqq')
        self.element_is_visible(self.locators.EMAIL).send_keys('qqq@qqq.qq')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('eeee')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('rrrrr')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

