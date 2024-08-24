import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://credence.in/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
time.sleep(2)

List = []

l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//a"))
# print(l)
time.sleep(3)
for r in range(1,l+1):
    Contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//a[" + str(r) + "]").text
    # print(Contact)
    List.append(Contact)

# print(List)

Number = "+91 7391053250"

if Number in List:
    print(List.index(Number))
    print("Number found--> Position -->" + str((List.index(Number) + 1)))
else:
    print("Number is Not Found")

driver.quit()

