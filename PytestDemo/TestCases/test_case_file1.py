import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Test_Pytest():

    @pytest.mark.skip
    def test_sum_001(self):
        a = 30
        b = 40
        sum = a+b
        print(sum)
        if sum == 80:
            assert True
        else:
            assert False

    @pytest.mark.xfail
    def test_sum_002(self):
        a = 3
        b = 5
        sum = a+b
        print(sum)
        if sum == 8:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_mul_003(self):
        a = 3
        b = 4
        mul = a*b
        print(mul)
        if mul == 12:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_credence_login_url_004(self):
        driver = webdriver.Chrome()
        time.sleep(3)
        driver.get("https://credence.in/")
        ### find enquiry numbers
        driver.find_element(By.XPATH,"//img[@src = '/website/images/enquiry.png']").click()

        l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        # print(l)

        contact_number_list = []
        for r in range(1,l+1):
            contact_number = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            # print(contact_number)
            contact_number_list.append(contact_number)
        print(contact_number_list)

        if '+91 7391053250' in contact_number_list:
            print(contact_number_list.index('+91 7391053250'))
            assert True
        else:
            assert False     ## check False condition also


        # if driver.title == "Credence":
        #     print("You are at right place")
        # else:
        #     print("You are at wrong place")


### pytest -v -n=3 -m sanity
### HTML report ---> --html=Reports/myreport.html