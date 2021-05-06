from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from time import sleep

def wait_for(condition_function, timeout=None):
    """Waits for a specific condition function to be true. Checks in 1 second increments.

    Args:
        condition_function (function): The condition to wait for.
    
    Kwargs:
        timeout (int or None): The maximum amount of time to wait, or None for no maxmium. None by default.
    
    Returns: True if the condition function was met, False if timed out."""
    i = 0
    while True:
        if condition_function():
            return True
        elif timeout is not None and i >= timeout:
            return False
        else:
            i += 1
            sleep(1)

def link_has_gone_stale(link):
    """Condition function to check if a Selenium link is still live."""
    def inner_func():
        try:
            link.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True
    return inner_func

def click_and_wait(btn):
    """Click on a button and wait for the next page to load."""
    btn.click()
    wait_for(link_has_gone_stale(btn))

def get_driver(headful=False):
    """Get a Selenium Chrome driver with some useful options set.
    
    Kwargs:
        headful (bool): Whether to launch the browser in headless mode. Default: False

    Returns:
        The WebDriver object. Note that the user is responsible for closing the session."""
    options = webdriver.chrome.options.Options()
    if not headful:
        options.add_argument('--headless')
    else:
        options.add_experimental_option("detach", True)
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
    })

    headful_str = "headful" if headful else "headless"

    return webdriver.Chrome(options=options)