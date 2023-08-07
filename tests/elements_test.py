# import time
#
# from pages.base_page import BasePage
#
#
# def test(driver):
#     page = BasePage(driver, 'https://google.com')
#     page.open()
#     time.sleep(3)

import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            print()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current_address does not match"
            assert permanent_address == output_per_addr, "the permanent_address does not match"

    class TestCheckbox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            time.sleep(3)

            print()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()

            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, "checkboxes have not been selected"

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            # assert output_no == "No", "'No' have not been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            time.sleep(5)
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):

            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            for _ in range(5):
                key_word = web_table_page.add_new_person()[random.randint(0, 5)]
                time.sleep(1)
                web_table_page.search_some_person(key_word)
                time.sleep(1)
                table_result = web_table_page.check_search_person()
                time.sleep(1)
                print(key_word)
                print(table_result)
                assert key_word in table_result or key_word in "".join(table_result), "the person was not found in the table"
                time.sleep(1)

                web_table_page.search_clear(key_word)
                # time.sleep(1)

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            time.sleep(1)
            web_table_page.search_some_person(lastname)
            time.sleep(1)
            age = web_table_page.update_person_info()
            time.sleep(1)
            row = web_table_page.check_search_person()
            time.sleep(1)
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'


    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            print(double)
            print(right)
            print(click)
            # assert double == ''
            # assert right ==
            # assert click ==