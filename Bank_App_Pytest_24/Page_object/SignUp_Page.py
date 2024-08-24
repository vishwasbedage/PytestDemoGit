from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# class SignUp_Class:
#     click_sign_up_xpath = "//a[normalize-space()='Sign Up']"
#     text_username_xpath = "//input[@id='username']"
#     text_password_xpath = "//input[@id='password']"
#     text_email_id = "email"
#     text_phone_id = "phone"
#     click_create_user_xpath = "//button[@type='submit']"
#     success_msg_xpath = "//div[@class='success-message']"
#
#     def __init__(self,driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver,10)
#
#     def Click_Signup(self):
#         self.driver.find_element(By.XPATH,self.click_sign_up_xpath).click()
#
#     def Enter_Username(self,username):
#         self.wait.until(expected_conditions.visibility_of_element_located(self.text_username_xpath))
#         self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)
#
#     def Enter_Password(self,password):
#         self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)
#
#     def Enter_Email(self,email):
#         self.driver.find_element(By.ID,self.text_email_id).send_keys(email)
#
#     def Enter_Phone(self,phone):
#         self.driver.find_element(By.ID,self.text_phone_id).send_keys(phone)
#
#     def Click_User_Creator(self):
#         self.driver.find_element(By.XPATH,self.click_create_user_xpath).click()
#
#     def Validate_User_Creation(self):
#         try:
#             success_msg = self.driver.find_element(By.XPATH,self.success_msg_xpath).text
#             return success_msg
#         except:
#             pass

from selenium.webdriver.common.by import By


class SignUp_Class:
    click_signup_XPATH = "//a[normalize-space()='Sign Up']"
    text_username_id = "username"
    text_password_id = "password"
    text_email_id = "email"
    text_phone_id = "phone"
    click_create_user_button_XPath = "//button[@type='submit']"
    success_message_class = "success-message"

    def __init__(self, driver):
        self.driver = driver

    def Click_Signup(self):
        self.driver.find_element(By.XPATH, self.click_signup_XPATH).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def Enter_Phone(self, phone):
        self.driver.find_element(By.ID, self.text_phone_id).send_keys(phone)

    def Click_CreateUser_Button(self):
        self.driver.find_element(By.XPATH, self.click_create_user_button_XPath).click()

    def Validate_User_Creation(self):
        try:
            success_msg = self.driver.find_element(By.CLASS_NAME, self.success_message_class).text
            return success_msg  # User created successfully
        except:
            pass







