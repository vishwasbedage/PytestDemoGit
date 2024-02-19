import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Pytest():
    @pytest.mark.regression
    def test_mul_005(self):
        a =5
        b = 4
        mul = a * b
        print(mul)
        if mul == 20:
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_credence_login_url_006(self):
        driver = webdriver.Chrome()
        time.sleep(3)
        driver.get("https://credence.in/")

        if driver.title == "Credence":
            print("You are at right place")
        else:
            print("You are at wrong place")

    def test_credence_login_url_007(self):
        driver = webdriver.Chrome()
        time.sleep(3)
        driver.get("https://credence.in/")
        ### find enquiry numbers
        driver.find_element(By.XPATH, "//img[@src = '/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        # print(l)

        contact_number_list = []
        for r in range(1, l + 1):
            contact_number = driver.find_element(By.XPATH,
                                                 "//div[@class='quickfinder-description gem-text-output']//p//a[" + str(
                                                     r) + "]").text
            # print(contact_number)
            contact_number_list.append(contact_number)
        print(contact_number_list)

        if '+91 7391053250' in contact_number_list:
            print(contact_number_list.index('+91 7391053250'))
            assert True
        else:
            assert False  ## check False condition also







