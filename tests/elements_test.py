# import time
#
# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://google.com')
#     page.open()
#     time.sleep(3)


import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)
