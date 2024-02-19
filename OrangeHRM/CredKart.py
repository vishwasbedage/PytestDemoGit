import time

from selenium import webdriver
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

driver.get("https://automation.credence.in/shop")
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
time.sleep(2)
driver.find_element(By.ID,"name").send_keys("Tejas")
time.sleep(2)

driver.find_element(By.ID,"email").send_keys("tejas1234@gmail.com")
time.sleep(2)

driver.find_element(By.ID,"password").send_keys("tejas1234")
time.sleep(2)

driver.find_element(By.ID,"password-confirm").send_keys("tejas1234")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

# if driver.title == "CredKart":
#     print("Registration is completed")
#
# else:
#     print("Registration is failed")


try:
    driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
    print("Registration is Completed")

except (NoSuchElementException,TimeoutException):
    print("Registration is Failed")



