import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_ele = driver.find_element(By.XPATH,"//select[@id='country']")

time.sleep(3)
drop_ele = Select(drop_ele)
time.sleep(3)

# drop_ele.select_by_visible_text("France")
# time.sleep(2)

# drop_ele.select_by_index(4)
# time.sleep(2)

# drop_ele.select_by_value("3")
# time.sleep(2)

### Capture the length of options
all_opt = drop_ele.options
print(len(all_opt))

### Capture the length of options
# for opt in all_opt:
#     print(opt.text)


###select option from list without using build in method

for opt in all_opt:
    if opt.text == "India":
        break


































