from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.python.org")

# element = driver.find_element(by=By.ID, value="id-search-field")
element = driver.find_element(by=By.ID, value="id-search-field")
# Clears any text in input box
element.clear()
element.send_keys("Django")
element.send_keys(Keys.ENTER)

driver.close()
