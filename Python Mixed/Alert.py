import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
#
# #Alter
# time.sleep(3)
# # print the alert message
# print(Alert(driver).text)
# # accept alert message (click on Ok button)
# Alert(driver).accept()
# print(driver.find_element(By.CSS_SELECTOR, "#result").text)
#


# # Confirmation

# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
# time.sleep(3)
# print(Alert(driver).text)
# # accept alert message (click on Ok button)
# #Alert(driver).accept()
# Alert(driver).dismiss()
# print(driver.find_element(By.CSS_SELECTOR, "#result").text)
#
# # Prompt
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
# time.sleep(3)
# Alert(driver).send_keys("Hi, I am Credence.")
# Alert(driver).accept()
# print(driver.find_element(By.CSS_SELECTOR, "#result").text)
# time.sleep(5)