from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.output_text = (By.CSS_SELECTOR, "h3.output") 
    def get_output(self) -> int:
        full_text = self.driver.find_element(*self.output_text).text
        result_number = int(full_text.split(":")[1].strip())
        return result_number