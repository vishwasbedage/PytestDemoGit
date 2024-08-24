import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage_class:

    Text_Username_Xpath = (By.XPATH,"//input[@placeholder='Username']")
    Text_Password_Xpath = (By.XPATH,"//input[@placeholder='Password']")
    Click_Login_Button_Xpath = (By.XPATH,"//button[normalize-space()='Login']")
    Menu_Xpath = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
    Click_Logout_Button_Xpath = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Enter_UserName(self,Username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Xpath))
        self.driver.find_element(*LoginPage_class.Text_Username_Xpath).send_keys(Username)

    def Enter_Password(self,Password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_Xpath))
        self.driver.find_element(*LoginPage_class.Text_Password_Xpath).send_keys(Password)

    def Click_Login_Button(self):
        self.driver.find_element(*LoginPage_class.Click_Login_Button_Xpath).click()

    def Menu_Button(self):
        self.driver.find_element(*LoginPage_class.Menu_Xpath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*LoginPage_class.Click_Logout_Button_Xpath).click()

    def Validate_Login_Status(self):
        try:
            time.sleep(2)
            # self.driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']")
            self.driver.find_element(*LoginPage_class.Menu_Xpath)
            time.sleep(2)
            print("User login test case is passed")
            return "LoginPass"

        except:
            print("User login test case is failed")
            return "LoginFail"

