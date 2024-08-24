import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/login")
driver.maximize_window()
time.sleep(3)

# Login
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("CredKart@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Cred12345")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

## Product
driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()

Product_quanity = Select(driver.find_element(By.XPATH,"//select[@class='quantity']"))
time.sleep(3)
Product_quanity.select_by_index(4)


Product_Price = driver.find_element(By.XPATH,"//div/table/tbody/tr[1]/td[4]").text
# print(Product_Price)
time.sleep(1)
Subtotal = driver.find_element(By.XPATH,"//div/table/tbody/tr[2]/td[4]").text
# print(Subtotal)

time.sleep(1)
Tax = driver.find_element(By.XPATH,"//div/table/tbody/tr[3]/td[4]").text
# print(Tax)

time.sleep(1)
Your_Total = driver.find_element(By.XPATH,"//div/table/tbody/tr[4]/td[4]").text
# print(Your_Total)
time.sleep(1)

print("Product_Price-->" + Product_Price)
print("Subtotal-->" + Subtotal)
print("Actual_Tax-->" + Tax)
print("Actual_Your_Total-->" + Your_Total)

Coveter_Product_P = Product_Price.replace('$','').replace(',','')
print("Product_Price_conv-->" + str(Coveter_Product_P))

Subtotal_cov = float(Subtotal.replace('$', '').replace(',', ''))
print("Subtotal_cov-->" + str(Subtotal_cov))

Actual_Tax_cov = float(Tax.replace('$', '').replace(',', ''))
print("Actual_Tax_cov-->" + str(Actual_Tax_cov))

Actual_Your_Total_cov = float(Your_Total.replace('$', '').replace(',', ''))
print("Actual_Your_Total_cov-->" + str(Actual_Your_Total_cov))

Expected_Tax = round((Subtotal_cov * 0.13),2)
# round(value,2)
print("Expected_Tax-->" + str(Expected_Tax))

if Actual_Tax_cov == Expected_Tax:
    print("System is calculating correct tax amount")
else:
    print("Wrong Tax value")

Expected_Your_Total = round((Expected_Tax + Coveter_Product_P),2)
print("Expected_Your_Total-->" + str(Expected_Your_Total))

if Actual_Your_Total_cov == Expected_Your_Total:
    print("System is calculating correct Your_Total amount")
else:
    print("Wrong Your_Total value")

# Expected_Tax = Actual_Tax
# Expected_Your_Total = Actual_Your_Total
