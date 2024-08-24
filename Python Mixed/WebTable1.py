
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

### Conut number of rows and columns

no_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
no_cols = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")

print(no_rows)
print(no_cols)


### find read sepecific rows in table

# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
# print(data)
#
# driver.close()

## read all rows and colunmns in data

print("printing All rows and cols in data")

for r in range(2,no_rows+1):
    for c in range(1,no_cols+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)

    print(data)

### read specific data  based on conditoon

for r in range(2,no_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print(book_name,"  ",author_name)











