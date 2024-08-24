import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Page_object.Login_Page import Login_Class
from Page_object.SignUp_Page import SignUp_Class
from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadConfigFile


# class Test_SignUp:
#     def test_BankApp_url_001(self,setup):
#         self.driver = setup
#         if self.driver.title == "Bank Application":
#             assert True
#         else:
#             assert False
#
#     def test_SignUp_002(self,setup):
#         self.driver = setup
#         self.su = SignUp_Class(self.driver)
#         self.su.Enter_Username("Demo12")
#         self.su.Enter_Password("Demo@123")
#         self.su.Enter_Email("demo1234321@gmail.com")
#         self.su.Enter_Phone("987859644")
#         self.su.Click_User_Creator()
#         # time.sleep(5)
#         if self.su.Validate_User_Creation() == "User created successfully":
#             assert True
#         else:
#             assert False
#
# import time
#
# from pageObjects.SignUp_Page import SignUp_Class


class Test_SignUp:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()
    Log = Log_Class.log_generator()

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_BankApp_Url_001(self, setup):
        """self.Log.debug("This is debug")
                self.Log.info("This is info")
                self.Log.warning("This is warning")
                self.Log.error("This is error")
                self.Log.critical("This is critical")"""

        self.Log.info("test_BankApp_Url_001 is started")
        self.Log.info("Opening Browser")
        self.driver = setup
        self.Log.info("Checking the title")
        if self.driver.title == "Bank Application":
            self.Log.info("test_BankApp_Url_001 is Passed")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_BankApp_Url_001_pass",attachment_type= AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_Url_001_Pass.png")
            self.Log.info("Testcase test_Login_001 is completed\n")

            assert True
        else:
            self.Log.info("test_BankApp_Url_001 is failed")
            self.Log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_BankApp_Url_001_pass",attachment_type= AttachmentType.PNG)  
            self.driver.save_screenshot(".\\Screenshots\\test_BankApp_Url_001_Fail.png")
            self.Log.info("Testcase test_Login_001 is completed\n")

            assert False

    @pytest.mark.regression
    @pytest.mark.group2
    def test_Signup_002(self, setup):
        self.Log.info("test_Signup_002 is Started")
        self.Log.info("Opening browser")
        self.driver = setup
        self.su = SignUp_Class(self.driver)
        self.Log.info("Click on signup link")
        self.su.Click_Signup()
        self.Log.info(generate_random_username())
        self.su.Enter_Username(generate_random_username())
        # self.Log.info("Enter Username")
        # self.su.Enter_Username("Demo55551")
        self.Log.info("Enter Password")
        self.su.Enter_Password("Demo555@")

        # self.Log.info("Enter email")
        self.Log.info(generate_random_email())
        self.su.Enter_Email(generate_random_email())
        # self.su.Enter_Email("Demo555@credence1.in")

        # self.Log.info("Enter phone number")
        self.Log.info(generate_random_phone_number())
        self.su.Enter_Password(generate_random_phone_number())
        # self.su.Enter_Phone("765665456")

        self.Log.info("Click create user")
        self.su.Click_CreateUser_Button()
        time.sleep(2)
        self.Log.info("Validate user creation is done successfully")
        if self.su.Validate_User_Creation() == "User created successfully":
            self.Log.info("test_Signup_002 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_pass.png ")
            self.Log.info("Testcase test_Login_002 is completed\n")

            assert True
        else:
            self.Log.info("test_Signup_002 is failed")
            self.driver.save_screenshot("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_002_fail.png ")
            self.Log.info("Testcase test_Login_002 is completed\n")

            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_Login_003(self, setup):
        self.Log.info("Testcase test_Login_003 is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.lp = Login_Class(self.driver)
        self.Log.info("Click on Login link")
        self.lp.Click_Login_Link()
        self.Log.info("Entering the username")
        self.lp.Enter_Username(self.Username)
        self.Log.info("Entering the password")
        self.lp.Enter_Password(self.Password)
        self.Log.info("Click on login button")
        self.lp.Click_Login_Button()
        self.Log.info("Checking the page title")
        if self.driver.title == "Dashboard":
            self.Log.info("Testcase test_Login_003 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_003_pass.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert True

        else:
            self.Log.info("Testcase test_Login_003 is failed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_Login_003_fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert False


import random
import string
import time

def generate_random_username(length=6):
    return 'User' + ''.join(random.choices(string.ascii_letters + string.digits,k=length))

def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain

def generate_random_phone_number():
    return ''.join(random.choices(string.digits,k=10))

