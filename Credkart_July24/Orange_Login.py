import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

try:
    time.sleep(2)
    driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    time.sleep(4)
    driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    print("User login test case is passed")
except:
    print("User login test case is failed")
