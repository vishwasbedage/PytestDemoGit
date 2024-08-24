import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("headless")
class Test003:
    # @pytest.mark.skip
    @pytest.mark.sanity
    def test_credencesite_010(self):
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.maximize_window()
        time.sleep(3)

        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        List = []
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a"))
        # print(l)
        time.sleep(3)
        for r in range(1, l + 1):
            Contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a[" + str(
                r) + "]").text
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

    @pytest.mark.web
    @pytest.mark.group1
    def test_Add_employee_011(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Rahul")
        driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("H")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Patil")
        time.sleep(3)

        ### Add photos
        file = r"C:\Users\SHREE\Downloads\BestCare.jpg"
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file)
        time.sleep(3)

        driver.find_element(By.XPATH,
                            "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
            "rahul")
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
            "Rahul123")
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys(
            "Rahul123")

        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        success_msg = driver.find_element(By.XPATH,
                                          "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']").text
        print(success_msg)

        if success_msg == "Successfully Saved":
            print("Add employee test case is passed")
        else:
            print("Add employee test case is failed")






        



