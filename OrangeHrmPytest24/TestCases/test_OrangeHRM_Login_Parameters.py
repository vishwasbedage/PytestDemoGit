import time  # Import the time module to introduce delays in the test

import pytest  # Import pytest for creating test cases
from selenium import webdriver  # Import the selenium webdriver for browser automation
from selenium.webdriver.common.by import By  # Import By for locating elements

from PageObjects.Login_Page import LoginPage_class
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import ReadConfig_Class

class Test_OrangeHRM_Login_params:  # Define the test class for parameterized OrangeHRM login tests

    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.smoke
    def test_OrangeHRM_Login_params_003(self, setup, getDataForLogin):
            self.log.info("test_OrangeHRM_Login_params_003 is started")  # Log the start of the test
            self.driver = setup  # Initialize the WebDriver using the setup fixture
            self.log.info("Opening the browser")  # Log the action of opening the browser

            self.lp = LoginPage_class(self.driver)  # Create an instance of the LoginPage class

            # print("Username-->" + self.Username)  # Print the username
            # print("Password-->" + self.Password)  # Print the password
            self.log.info("Entering Username-->" + getDataForLogin[0])  # Log the action of entering the username from the test data

            self.lp.Enter_UserName(getDataForLogin[0])  # Enter the username using the page object method

            self.log.info("Entering Password-->" + getDataForLogin[1])  # Log the action of entering the password from the test data
            self.lp.Enter_Password(getDataForLogin[1])  # Enter the password using the page object method

            self.log.info("Clicking on login button")  # Log the action of clicking the login button
            self.lp.Click_Login_Button()  # Click the login button using the page object method
            self.log.info("Verifying the login status")  # Log the verification of the login status

            if self.lp.Validate_Login_Status() == "LoginPass" and getDataForLogin[2] == "Login_Pass":  # Check if login passed and expected result is "Login_Pass"
                self.log.info("test_OrangeHRM_Login_params_003 is passed")  # Log the success of the test
                time.sleep(2)  # Wait for 2 seconds
                self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_pass.png")  # Save a screenshot
                self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
                self.lp.Menu_Button()  # Click the menu button using the page object method
                self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
                self.lp.Click_Logout_Button()  # Click the logout button using the page object method
                assert True  # Assert the test as passed

            elif self.lp.Validate_Login_Status() == "LoginPass" and getDataForLogin[2] == "Login_Fail":  # Check if login passed and expected result is "Login_Fail"
                self.log.info("test_OrangeHRM_Login_params_003 is failed")  # Log the failure of the test
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")  # Save a screenshot
                self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
                self.lp.Click_Login_Button()  # Click the menu button using the page object method
                self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
                self.lp.Click_Logout_Button()  # Click the logout button using the page object method
                assert False  # Assert the test as failed

            elif self.lp.Validate_Login_Status() == "LoginFail" and getDataForLogin[2] == "Login_Pass":  # Check if login failed and expected result is "Login_Pass"
                self.log.info("test_OrangeHRM_Login_params_003 is failed")  # Log the failure of the test
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")  # Save a screenshot
                assert False  # Assert the test as failed

            elif self.lp.Validate_Login_Status() == "LoginFail" and getDataForLogin[2] == "Login_Fail":  # Check if login failed and expected result is "Login_Fail"
                self.log.info("test_OrangeHRM_Login_params_003 is passed")  # Log the success of the test
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_pass.png")  # Save a screenshot
                assert True  # Assert the test as passed
            self.log.info("Closing the browser")  # Log the action of closing the browser
            self.driver.quit()  # Close the browser
            self.log.info("test_OrangeHRM_Login_params_003 is completed")  # Log the completion of the test







