

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
# from selenium.webdriver.common.by import By
#
driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://www.amazon.in/")
# time.sleep(3)
#
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile phone")
# time.sleep(3)
# driver.find_element(By.XPATH,"//div[@aria-label='mobile phone']").click()



driver.get("https://www.facebook.com/")
time.sleep(5)

driver.find_element(By.ID,"email").send_keys("vishwas@gmail.com")
time.sleep(3)
driver.find_element(By.NAME,"pass").send_keys("Vishwas123")
time.sleep(3)
driver.find_element(By.NAME,"login").click()
time.sleep(3)
driver.close()

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://automation.credence.in")
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Login").click()
# time.sleep(3)
# driver.find_element(By.ID,"email").send_keys("test@credence.in")
# time.sleep(3)
# driver.find_element(By.ID,"password").send_keys("test@123")
# time.sleep(3)
# driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
# time.sleep(3)
#
# print("Login successfully passed ")
# driver.close()


# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path="C:\\Users\\yusuf\\Downloads\\chromedriver_win32")
# driver.get("https://www.facebook.com/")
# time.sleep(5)
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #
# import time
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# browser = webdriver.Chrome(options=options)
# # #
# browser.get("https://www.facebook.com/")
# browser.maximize_window()
#
# username= "yusftamboli@gmail.com"
# password= "Tester123@"
# browser.find_element(By.NAME,"email").send_keys(username)
# time.sleep(5)
# browser.find_element(By.NAME,"pass").send_keys(password)
# time.sleep(5)
# browser.find_element(By.NAME,"login").click()
# time.sleep(10)
# browser.close()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# import time
# firefox_options = Options()
#
# browser = webdriver.Firefox(options=firefox_options)
#
#
# url = 'http://automation.credence.in'
# browser.get(url)
# browser.find_element(By.LINK_TEXT, "Login").click()
# browser.find_element(By.NAME, "email").send_keys("test@credence.in")
# time.sleep(2)
# browser.find_element(By.NAME, "password").send_keys("test@123")
# browser.find_element(By.NAME, "password").send_keys("tet@123")
#
# time.sleep(2)
# browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
#
# browser.maximize_window()
# print("Login Test Successfully Passed")
# browser.close()
# #



# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# import time
# #
# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# #
# url = 'http://automation.credence.in'
# browser.get(url)
# browser.find_element(By.LINK_TEXT, "Login").click()
# browser.find_element(By.NAME, "email").send_keys("test@credence.in")
# time.sleep(2)
# browser.find_element(By.NAME, "password").send_keys("test@123")
#
# time.sleep(2)
# browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
#
# browser.maximize_window()
# time.sleep(5)
# 
# print("Login Test Successfully Passed")
# browser.close()
#





