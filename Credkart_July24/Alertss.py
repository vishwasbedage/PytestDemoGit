import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

### Click For JS Alert
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()

#Alert
time.sleep(3)
alert = Alert(driver).text
print(alert)

Alert(driver).accept()
sucess_msg = driver.find_element(By.XPATH,"//p[@id='result']").text
print(sucess_msg)

### Click For JS Confirm
driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
time.sleep(3)
alert = Alert(driver).text
print(alert)
time.sleep(3)
# Alert(driver).accept()
Alert(driver).dismiss()

succ_msg = driver.find_element(By.XPATH,"//p[@id='result']").text
print(succ_msg)


### Click For Js Prompt

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(3)
alert = Alert(driver).text
time.sleep(3)

Alert(driver).send_keys("Hi I Am Vishwas")
time.sleep(3)
Alert(driver).accept()

succs_msg = driver.find_element(By.XPATH,"//p[@id='result']").text
print(succs_msg)
time.sleep(3)


