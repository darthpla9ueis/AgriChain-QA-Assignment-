import pytest
from selenium import webdriver
from pages.input_page import InputPage
from pages.result_page import ResultPage

@pytest.fixture
def browser():
        driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_standard_repeating_string(browser):
    input_page = InputPage(browser)
    result_page = ResultPage(browser)
    test_string = "abcabcabcb"
    expected_result = 3

    input_page.load()
    input_page.calculate_substring(test_string)

    actual_result = result_page.get_output_value()
    assert actual_result == expected_result