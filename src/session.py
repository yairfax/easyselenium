from .functions import *
from traceback import print_exc

class Session:
    """A Selenium Chrome driver that can be used with a with clause"""
    def __init__(self, headful=False):
        self.driver = get_driver(headful=headful)

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        if value:
            print_exc
        if self.driver:
            self.driver.close()
