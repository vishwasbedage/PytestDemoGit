import time

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://testmy.net/")
# wait applicable for all the elements
# total it takes 40sec--- if element loads at 21st sec then it will not take complete 40 sec proceed for next.
# if element does not load in 40 secs then system will raise exception
driver.implicitly_wait(200)


# click on test my internet
driver.find_element(By.XPATH, "//a[@id='testBtnMn']").click()
# click on combined
driver.find_element(By.XPATH, "//a[@title='Upload & Download Speed Test']").click()

# time.sleep(40) --hard time we have to wait to complete 40 sec
# wait = WebDriverWait(driver, 30)  # 10 seconds maximum waiting time
# element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Details &']")))
# click on detail & share
driver.find_element(By.XPATH, "//span[normalize-space()='Details &']").click()

print(driver.find_element(By.XPATH, "//textarea[@name='contactDetails']").get_attribute('value'))
