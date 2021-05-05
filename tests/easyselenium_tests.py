import unittest
from selenium import webdriver
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

def get_driver():
    options = webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
    })

    return webdriver.Chrome(options=options)


class EasySeleniumTests(unittest.TestCase):
    def test_wait_for(self):
        self.assertTrue(wait_for(make_closure(2), timeout=3))
        self.assertFalse(wait_for(make_closure(2), timeout=1))

    def test_click_and_wait(self):
        driver = get_driver()

        driver.get("https://www.google.com")
        btn = [el for el in driver.find_elements_by_class_name("MV3Tnb") if el.text.lower() == "about"][0]

        click_and_wait(btn)

        self.assertTrue("about.google" in driver.current_url)

        driver.close()

    def test_click_nowait(self):
        driver = get_driver()

        driver.get("https://www.google.com")
        btn = [el for el in driver.find_elements_by_class_name("MV3Tnb") if el.text.lower() == "about"][0]

        btn.click()

        self.assertFalse("about.google" in driver.current_url)

        driver.close()
        
if __name__ == "__main__":
    unittest.main()