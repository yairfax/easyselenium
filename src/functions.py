from selenium.common.exceptions import StaleElementReferenceException
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