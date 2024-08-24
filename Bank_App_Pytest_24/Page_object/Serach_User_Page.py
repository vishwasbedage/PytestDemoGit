from selenium.webdriver.common.by import By


class Search_User_Class:
    click_link_user_mangmnt_xpath = "//a[normalize-space()='User Management']"
    Enter_Username_xpath = "//input[@id='username']"
    click_Search_User_Button_xpath = "//button[@type='submit']"
    Validate_Serach_User_Page_Title_css = "div[class='container'] h2"

    def __init__(self,driver):
        self.driver = driver

    def Click_Link_User_Management(self):
        self.driver.find_element(By.XPATH,self.click_link_user_mangmnt_xpath).click()

    def Enter_Username(self,username):
        self.driver.find_element(By.XPATH,self.Enter_Username_xpath).send_keys(username)

    def Click_SerachUser_Button(self):
        self.driver.find_element(By.XPATH,self.click_Search_User_Button_xpath).click()

    def Validate_Search_User(self):
        title = self.driver.find_element(By.CSS_SELECTOR,self.Validate_Serach_User_Page_Title_css).text
        if title == "Edit User":
            return "pass"
        else:
            return "fail"
        




