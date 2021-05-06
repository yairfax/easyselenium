import unittest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from easy_selenium import *
from time import sleep

def make_closure(timeout):
    i = 0
    def cond():
        nonlocal i
        if i < timeout:
            sleep(1)
            i += 1
            return False
        return True
    
    return cond

class EasySeleniumTests(unittest.TestCase):
    def test_wait_for(self):
        self.assertTrue(wait_for(make_closure(2), timeout=3))
        self.assertFalse(wait_for(make_closure(2), timeout=1))

    def test_click_and_wait(self):
        with get_driver() as driver:
            driver.get("https://www.google.com")
            btn = [el for el in driver.find_elements_by_class_name("MV3Tnb") if el.text.lower() == "about"][0]

            click_and_wait(btn)

            self.assertIn("about.google", driver.current_url)

    def test_click_nowait(self):
        with get_driver() as driver:
            driver.get("https://www.google.com")
            btn = [el for el in driver.find_elements_by_class_name("MV3Tnb") if el.text.lower() == "about"][0]

            btn.click()

            self.assertNotIn("about.google", driver.current_url)

if __name__ == "__main__":
    unittest.main()