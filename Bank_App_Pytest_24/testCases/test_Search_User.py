import time

import pytest

from Page_object.Login_Page import Login_Class
from Page_object.Serach_User_Page import Search_User_Class
from Utilities.readProperties import ReadConfigFile


class Test_Search_User:
    username = ReadConfigFile.GetUsername()
    password = ReadConfigFile.GetPassword()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_004(self,setup):
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.lp.Enter_Username(self.username)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login_Button()

        self.su = Search_User_Class(self.driver)
        self.su.Click_Link_User_Management()
        self.su.Enter_Username("Tushar")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")   ## for scroll up page upto element
        time.sleep(3)
        self.su.Click_SerachUser_Button()
        if self.su.Validate_Search_User() == "pass":
            assert True
        else:
            assert False




    


