import time

import pytest

from Page_object.Login_Page import Login_Class
from Page_object.Serach_User_Page import Search_User_Class
from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadConfigFile


class Test_Search_User_Params:
    username = ReadConfigFile.GetUsername()
    password = ReadConfigFile.GetPassword()
    Log = Log_Class.log_generator()

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_search_user_005(self,setup,getDataForSearchUser):
        self.Log.info("test_search_user_005 is started")
        self.Log.info("Opening the browser")
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.Log.info("Click on login link")
        self.lp.Click_Login_Link()
        self.Log.info("Enter Username")
        self.lp.Enter_Username(self.username)
        self.Log.info("Enter Password")
        self.lp.Enter_Password(self.password)
        self.Log.info("click on login button")
        self.lp.Click_Login_Button()

        self.su = Search_User_Class(self.driver)

        self.Log.info("Click on User management link")
        self.su.Click_Link_User_Management()

        search_Username = getDataForSearchUser[0]
        self.Log.info("Searching the username ")
        # print(search_Username)
        expected_result = getDataForSearchUser[1]
        self.Log.info("Getting Expected Result")
        # print(expected_result)

        self.su.Enter_Username(search_Username)
        self.Log.info("Entering the Username for searching")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        self.Log.info("Clicking On search Button")
        self.su.Click_SerachUser_Button()
        self.Log.info("Validate Username")
        if self.su.Validate_Search_User() == "pass" and expected_result == "pass":
            self.Log.info("test_search_user_005 is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user_005_Pass.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert True
        elif self.su.Validate_Search_User() == "pass" and expected_result == "fail":
            self.Log.info("test_search_user_005 is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user_005_Fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert False
        elif self.su.Validate_Search_User() == "fail" and expected_result == "pass":
            self.Log.info("test_search_user_005 is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user_005_Fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert False
        elif self.su.Validate_Search_User() == "fail" and expected_result == "fail":
            self.Log.info("test_search_user_005 is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user_005_Fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert True




