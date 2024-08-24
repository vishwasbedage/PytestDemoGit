import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

## Date of birth

driver.find_element(By.XPATH,"//input[@id='dob']").click()

months = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
months.select_by_visible_text("Mar")
time.sleep(2)

years = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
years.select_by_visible_text("1994")
time.sleep(2)

all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td//a")

for date in all_dates:
    if date.text == "27":
        date.click()
        break
time.sleep(2)







