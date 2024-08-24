import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
#time.sleep(4)

driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()

time.sleep(4)
##To capture all windows in browser
Select_window = driver.window_handles

# To switch  specific window by index  (2nd window)
driver.switch_to.window(Select_window[1])
print(driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
#time.sleep(4)
# (1st window)
driver.switch_to.window(Select_window[0])
#time.sleep(4)
print(driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text)
#time.sleep(4)
driver.close()
# driver.close vs driver.quit()

time.sleep(40)