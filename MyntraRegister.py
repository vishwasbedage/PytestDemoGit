import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.myntra.com/register")
time.sleep(3)



