import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        incr_element = driver.find_element(By.ID, "increase")
        initial_value = int(driver.find_element(By.TAG_NAME, "h1").text)
        incr_element.click()
        final_value = int(driver.find_element(By.TAG_NAME, "h1").text)
        self.assertEqual(initial_value + 1, final_value)

if __name__ == "__main__":
    unittest.main()



