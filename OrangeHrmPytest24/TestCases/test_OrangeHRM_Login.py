import time

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_Page import LoginPage_class
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import ReadConfig_Class


class Test_Orange_HRM:

    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_Orange_Hrm_Login_001(self,setup):
        # self.log.debug("This is debug")
        # self.log.info("This is INFO")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        self.log.info("test_Orange_Hrm_Login_001 is started")

        # driver = webdriver.Chrome(options=chrome_options)
        self.driver = setup
        self.log.info("Opening the Browser")
        time.sleep(2)
        if self.driver.title == "OrangeHRM":
            self.log.info("test_Orange_Hrm_Login_001 is Verified")
            self.log.info("test_Orange_Hrm_Login_001 is passed,user is landed on correct url")
            # print("driver title --> ",self.driver.title)
            self.log.info("Taking The ScreenShot")
            self.driver.save_screenshot("OrangeHrmPytest24\\Screenshots\\test_Orange_Hrm_Login_001.png")
            assert True

        else:
            self.log.info("test_Orange_Hrm_Login_001 is failed,user is landed on wrong url")
            self.log.info("Taking The ScreenShot")
            self.driver.save_screenshot("OrangeHrmPytest24\\Screenshots\\test_Orange_Hrm_Login_001.png")
            assert False
        self.log.info("Closing the browser")
        self.driver.quit()
        self.log.info("test_Orange_Hrm_Login_001 is Completed")

    @pytest.mark.sanity
    def test_Orange_Hrm_Login_002(self,setup):
        self.log.critical("test_Orange_Hrm_Login_002 is started")
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = LoginPage_class(self.driver)
        time.sleep(2)
        print("Username --> " + self.Username)
        print("Password --> " + self.Password)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_UserName(self.Username)  ## Admin
        self.log.info("Entering Username -->" + self.Username)

        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Enter_Password(self.Password)   ##admin123
        self.log.info("Entering Username -->" + self.Password)

        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.lp.Click_Login_Button()
        self.log.info("Clicking on Login Button")
        self.log.info("Verifying login Status")
        if self.lp.Validate_Login_Status() == "LoginPass":
            self.log.info("test_Orange_Hrm_Login_002 is Passed")
            self.lp.Menu_Button()
            self.log.info("clicking on Menu Button")
            self.lp.Click_Logout_Button()
            self.log.info("Clicking on logout button")
            # assert True
            self.log.info("Taking on screenshot")
            self.driver.save_screenshot("OrangeHrmPytest24\\Screenshots\\test_Orange_Hrm_Login_002.png")
        else:
            self.log.info("test_Orange_Hrm_Login_002 is failed")
            self.log.info("Taking on screenshot")
            self.driver.save_screenshot("OrangeHrmPytest24\\Screenshots\\test_Orange_Hrm_Login_002.png")
            # assert False
        self.log.info("Browser is closed")
        self.driver.quit()
        self.log.info("test_Orange_Hrm_Login_002 is Completed")




