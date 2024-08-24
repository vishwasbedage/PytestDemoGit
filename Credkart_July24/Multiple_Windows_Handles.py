import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
driver.switch_to.window(driver.window_handles[0])


# driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
# driver.switch_to.window(driver.window_handles[2])
# driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
# driver.switch_to.window(driver.window_handles[3])
# driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
# driver.switch_to.window(driver.window_handles[4])
# driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()


## Capture all windows
# driver.window_handles
# time.sleep(4)
#
# driver.switch_to.window(driver.window_handles[0])
# text1 = driver.find_element(By.XPATH,"//div[@class='large-4 large-centered columns']//div[1]").text
# print(text1)
# ##Powered by Elemental Selenium
# time.sleep(4)
#
# driver.switch_to.window(driver.window_handles[1])
# text2 = driver.find_element(By.XPATH,"//h3[normalize-space()='New Window']").text
# print(text2)
# ##New Window
#
# # driver.close()
# driver.quit()