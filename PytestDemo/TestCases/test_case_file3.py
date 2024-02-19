
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from selenium.webdriver.common.service import Service
headless_option = webdriver.ChromeOptions()
headless_option.add_argument("headless")


class Test_Pytest():
    @pytest.mark.group1
    def test_mul_008(self):
        a = 5
        b = 5
        mul = a * b
        print(mul)
        if mul == 25:
            assert True
        else:
            assert False

    @pytest.mark.group1
    def test_orange_hrm_009(self):
        driver = webdriver.Chrome(options=headless_option)
        driver.maximize_window()
        time.sleep(2)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(3)

        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    @pytest.mark.group1
    def test_Registration_010(self):
        driver = webdriver.Chrome(options=headless_option)
        driver.maximize_window()
        time.sleep(3)

        driver.get("https://automation.credence.in/shop")
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Tejas")
        time.sleep(2)

        driver.find_element(By.ID, "email").send_keys("tejas1234@gmail.com")
        time.sleep(2)

        driver.find_element(By.ID, "password").send_keys("tejas1234")
        time.sleep(2)

        driver.find_element(By.ID, "password-confirm").send_keys("tejas1234")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # if driver.title == "CredKart":
        #     print("Registration is completed")
        #
        # else:
        #     print("Registration is failed")

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Registration is Completed")

        except (NoSuchElementException, TimeoutException):
            print("Registration is Failed")






