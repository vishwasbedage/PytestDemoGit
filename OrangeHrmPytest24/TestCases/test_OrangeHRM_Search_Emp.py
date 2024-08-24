import pytest

from PageObjects.Add_Emp_Page import AddEmp_Class
from PageObjects.Login_Page import LoginPage_class
from PageObjects.Search_Emp_Page import SearchEmp_Class
from utilities.LoggerFile import LogGenerator
from utilities.ReadConfigFile import ReadConfig_Class


class Test_SearchEmp:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_SearchEmp_006(self,setup):
        self.log.info("test_AddEmp_006 testcase is started")
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

        self.se = SearchEmp_Class(self.driver)
        Emp_id = "03971"
        self.se.Enter_EmpID(Emp_id)
        self.se.Click_Search_Emp()
        if self.se.Search_Result() == Emp_id:
            assert True
        else:
            assert False


# logs are pending for above testcase
# Add emp  --> params and excel
# search emp --> params and excel
## msg success
