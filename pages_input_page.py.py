from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InputPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://agrichain.com/qa/input
        self.input_box = (By.ID, "string-input")
        self.submit_button = (By.TAG_NAME, "button")

    def load(self):
        self.driver.get(self.url)

    def calculate_substring(self, text: str):
        self.driver.find_element(*self.input_box).send_keys(text)
        self.driver.find_element(*self.submit_button).click()