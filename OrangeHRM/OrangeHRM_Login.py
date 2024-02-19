import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)

driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

