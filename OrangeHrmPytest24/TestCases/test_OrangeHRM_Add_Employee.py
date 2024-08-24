import pytest

from PageObjects.Add_Emp_Page import AddEmp_Class
from PageObjects.Login_Page import LoginPage_class
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import ReadConfig_Class


class Test_AddEmp:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    Photo_File_path = r"C:\Users\SHREE\Downloads\BestCare.jpg"

    @pytest.mark.regression
    def test_AddEmp_005(self,setup):
        self.log.info("test_AddEmp_005 testcase is started")
        self.driver = setup

        self.log.info("Opening browser")
        self.lp = LoginPage_class(self.driver)

        self.log.info("Enter Username")
        self.lp.Enter_UserName(self.Username)

        self.log.info("Enter Password")
        self.lp.Enter_Password(self.Password)

        self.log.info("Click on login Button")
        self.lp.Click_Login_Button()

        self.ae = AddEmp_Class(self.driver)
        self.log.info("Click on PIM Button")
        self.ae.Click_PIM()
        self.log.info("Click on AddEmp  Button")
        self.ae.Click_AddEmp_Button()

        self.log.info("Enter FirstName")
        self.ae.Enter_FirstName("Virat")
        self.log.info("Enter MiddleName")
        self.ae.Enter_MiddleName("K")
        self.log.info("Enter LastName")
        self.ae.Enter_LastName("King")

        self.log.info("Uploading Image")
        self.ae.Upload_Photo_File(self.Photo_File_path)
        self.log.info("Click On Save Button")
        self.ae.Click_Save_Button()

        self.log.info("Validating the success message for add emp ")
        if self.ae.Validate_AddEmp_SuccessMessage() == "Successfully Saved":
            self.log.info("test_AddEmp_005 testcase is passed")
            assert True
        else:
            self.log.info("test_AddEmp_005 testcase is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_AddEmp_005_fail.png")
            assert False
        self.log.info("test_AddEmp_005 testcase is completed")






