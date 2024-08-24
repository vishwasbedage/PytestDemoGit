import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/shop")
driver.maximize_window()
time.sleep(3)

## Login
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("CredKart@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Cred12345")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='remember']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()


###Product
driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()

Product_quanity = Select(driver.find_element(By.XPATH,"//select[@class='quantity']"))
time.sleep(3)
Product_quanity.select_by_index(4)

Continue_Shop = driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
time.sleep(3)

# driver.find_element(By.XPATH,"//h3[normalize-space()='Electric Guitar']").click()
# time.sleep(3)

driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()

time.sleep(10)
# HeadPhone = driver.find_element(By.XPATH,"//h3[normalize-space()='Headphones']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]").click()
# time.sleep(5)
# Product_quanity1 = Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
# Product_quanity1.select_by_index(2)


# driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()





