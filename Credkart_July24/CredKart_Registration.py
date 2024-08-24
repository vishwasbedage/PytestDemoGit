import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/shop")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Credence12345")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("CredKart@gmail.com")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Cred12345")
driver.find_element(By.XPATH,"//input[@id='password-confirm']").send_keys("Cred12345")
time.sleep(3)

driver.find_element(By.XPATH,"//button[@type='submit']").click()




