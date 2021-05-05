# Easy Selenium

Easy Selenium is a package with utility functions to make Selenium easier to use.

The most useful function in this package is `click_and_wait(btn)`, which clicks on the provided button and then waits until the next page loads.

```python
from selenium import webdriver
from easy_selenium import *

driver = webdriver.Chrome()
driver.get("https://www.google.com")

btn = driver.find_element_by_id("login")
click_and_wait(btn)
```
