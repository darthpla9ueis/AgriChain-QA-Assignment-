# This is for "Test Function 07" from the uploaded xlsx file for automated testing

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://agrichain.com/qa/input")

input_box = driver.find_element(By.ID, "stringInput")
input_box.send_keys("!@#$!@#")

submit_button = driver.find_element(By.ID, "submitbutton")
submit_button.click()

result_element = driver.find_element(By.ID, "outputresult")
result = result_element.text
if result == "output is: 4":
    print("Test Passed. The result is 'output is: 4', which is correct.")
else:
    print(f"Test Failed. Expected 'output is: 4' but got '{result}'.")
driver.quit()