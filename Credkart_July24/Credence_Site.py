import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://credence.in/")
time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
time.sleep(2)
List = []
l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a"))
#print(l)

time.sleep(2)
for r in range (1, l+1):
    Contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a[" + str(r) +"]").text
    #print(Contact)
    List.append(Contact)

print(List)

Number = "+91 7391053251"

if Number in List:
    print(List.index(Number))
    print("Number found--> Position -->" + str((List.index(Number) + 1)))
else:
    print("Number Not Found")


driver.quit()