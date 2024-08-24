
import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class TestClass5:

    @pytest.mark.web
    @pytest.mark.group2
    def test_OrangeHrm_Login_014(self):
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
            time.sleep(4)
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            print("User login test case is passed")
            assert True
        except:
            print("User login test case is failed")
            assert False


        driver.quit()


