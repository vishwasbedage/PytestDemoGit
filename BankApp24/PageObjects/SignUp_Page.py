from selenium.webdriver.common.by import By

class Sign_Up_Class:
    Click_SignUp_Xpath = "//a[normalize-space()='Sign Up']"
    Click_UserName_Xpath = "//input[@id='username']"
    Click_Password_Xpath = "//input[@id='password']"
    Click_Email_Xpath = "//input[@id='email']"
    Click_Phone_Xpath = "//input[@id='phone'] "
    Click_CreateUser_Button_Xpath = "//button[@type='submit']"
    success_msg_XPATH = "//div[@class='success-message']"

    def __init__(self,driver):
        self.driver = driver

    def Click_SignUp(self):
        self.driver.find_element(By.XPATH,self.Click_SignUp_Xpath).click()

    def Enter_Username(self,username):
        self.driver.find_element(By.XPATH,self.Click_UserName_Xpath).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(By.XPATH,self.Click_Password_Xpath).send_keys(password)

    def Enter_Email(self,email):
        self.driver.find_element(By.XPATH,self.Click_Email_Xpath).send_keys(email)

    def Enter_Phone(self,phone):
        self.driver.find_element(By.XPATH,self.Click_Phone_Xpath).send_keys(phone)

    def Click_Create_User(self):
        self.driver.find_element(By.XPATH,self.Click_CreateUser_Button_Xpath).click()

    

