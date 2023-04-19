import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class NoTest1:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def click_yes(self):
        base_url = 'https://demoqa.com/radio-button'
        self.driver.get(base_url)
        self.driver.maximize_window()
        time.sleep(2)

        print('Start test')

        button_yes = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Yes"]')))
        button_yes.click()
        time.sleep(3)
        print('Click button YES')


test = NoTest1()
test.click_yes()
