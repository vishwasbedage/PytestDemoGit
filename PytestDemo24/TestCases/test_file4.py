import time
from selenium import webdriver
import pytest
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from TestCases.test_file3 import chrome_options


class Test004:
    @pytest.mark.sanity
    def test_Credence012(self):
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        try:
            driver.find_element(By.XPATH, "//img[@alt='Credence IT']")
            assert True
        except:
            assert False
        driver.quit()

    @pytest.mark.regression
    def test_Credkart_Login013(self):
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/login")
        # 3 Enter Email Id
        driver.find_element(By.ID, "email").send_keys("2may2024@gmail.com")
        # 4 Enter Password
        driver.find_element(By.ID, "password").send_keys("Test@123")
        time.sleep(3)
        # 5 Click on Login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 6 Verify Login
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login test cases pass")
            assert True
        except:
            print("Login test cases fail")
            assert False

        # 9 quit the driver
        driver.quit()



