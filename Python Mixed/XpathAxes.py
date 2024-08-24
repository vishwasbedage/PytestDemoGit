
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

## Self node
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Zensar Technologies')]/self::a").text
# print(text_msg)

## Parent
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Zensar Technologies')]/parent::td").text
# print(text_msg)

## Ancestor








