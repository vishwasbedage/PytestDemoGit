
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Digital downloads ").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

## Find total number of links

links = driver.find_elements(By.TAG_NAME,"a")
print("Total number of links",len(links))

# links =driver.find_elements(By.XPATH,"//a")
# print("Total number of links",len(links))

##3 ptint all links

for link in links:
    print(link.text)





