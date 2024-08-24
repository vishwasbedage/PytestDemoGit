import time

import pytest

from PageObjects.Login_Page import LoginPage_class
from utilities import Excel_Utils
from utilities.LoggerFile import LogGenerator


class Test_Orange_HRM_Login_DDT:
    log = LogGenerator.loggen()
    file_path = ".\\TestCases\\TestData\\Test Data.xlsx"

    @pytest.mark.regression
    def test_OrangeHRM_DDT_004(self,setup):
        self.log.info("test_OrangeHRM_DDT_004 is started")
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = LoginPage_class(self.driver)

        self.rows = Excel_Utils.getrowCount(self.file_path,"Login Data")
        print("Number of rows in Excel Data --> " + str(self.rows))
        List_Status = []
        for r in range(2,self.rows+1):
            self.username = Excel_Utils.getreadData(self.file_path,"Login Data",r,2)
            self.password = Excel_Utils.getreadData(self.file_path,"Login Data",r,3)
            self.Excel_Result = Excel_Utils.getreadData(self.file_path,"Login Data",r,4)
            # print("username ---> " + "loop--->" + str(r) + "--" + str(self.username))
            # print("password ---> " + "loop--->" + str(r) + "--" + str(self.password))
            # print("Excel_Result ---> " + "loop--->" + str(r) + "--" + str(self.Excel_Result))
            # print("___________________________________________________________")

            self.log.info("Entering Password --> " + self.username)
            self.lp.Enter_UserName(self.username)

            self.log.info("Entering Password --> " + self.password)
            self.lp.Enter_Password(self.password)
            time.sleep(3)
            self.log.info("Clicking on login Button")
            self.lp.Click_Login_Button()

            self.log.info("Verifying login status")
            if self.lp.Validate_Login_Status() == "LoginPass" and self.Excel_Result == "Login_Pass":
                List_Status.append("Pass")
                Excel_Utils.getwriteData(self.file_path,"Login Data","r",5,"Pass")
                self.log.info("test_OrangeHRM_DDT_004 is passed")
                self.log.info("Taking the Screenshot ")
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_DDT_004_Pass.png")
                self.log.info("Clicking on Menu Button")
                self.lp.Menu_Button()
                self.log.info("Clicking on Logout Button")
                self.lp.Click_Logout_Button()

            elif self.lp.Validate_Login_Status() == "LoginPass" and self.Excel_Result == "Login_Fail":
                List_Status.append("Fail")
                Excel_Utils.getwriteData(self.file_path,"Login Data","r",5,"Fail")
                self.log.info("test_OrangeHRM_DDT_004 is failed")
                self.log.info("Taking the Screenshot ")
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_DDT_004_Fail.png")

            elif self.lp.Validate_Login_Status() == "LoginFail" and self.Excel_Result == "Login_Pass":
                List_Status.append("Fail")
                Excel_Utils.getwriteData(self.file_path,"Login Data","r",5,"Fail")
                self.log.info("test_OrangeHRM_DDT_004 is failed")
                self.log.info("Taking the Screenshot ")
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_DDT_004_Fail.png")

            elif self.lp.Validate_Login_Status() == "LoginFail" and self.Excel_Result == "Login_fail":
                List_Status.append("Pass")
                Excel_Utils.getwriteData(self.file_path,"Login Data","r",5,"Pass")
                self.log.info("test_OrangeHRM_DDT_004 is passed")
                self.log.info("Taking the Screenshot ")
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_DDT_004_Pass.png")
            self.log.info("Closing Browser")

        print(List_Status)
        if "Fail" not in List_Status:
            self.log.info("test_OrangeHRM_DDT_004 is passed")
            assert True
        else:
            self.log.info("test_OrangeHRM_DDT_004 is failed")
            assert False
        self.driver.quit()
        self.log.info("test_OrangeHRM_DDT_004 is Completed")













