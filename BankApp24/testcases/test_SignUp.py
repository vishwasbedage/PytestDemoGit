from PageObjects.SignUp_Page import Sign_Up_Class


class Test_BankApp_SingUp:
    def test_SignUp_001(self,setup):
        self.driver = setup
        self.su = Sign_Up_Class(self.driver)
        self.su.Click_SignUp()
        self.su.Enter_Username("Demo12234")
        self.su.Enter_Password("Demo@12234")
        self.su.Enter_Email("demo12234@gmail.com")
        self.su.Enter_Phone("989898123")
        self.su.Click_Create_User()
        if self.driver == "Login":
            assert True
        else:
            assert False




