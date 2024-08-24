from Page_object.Login_Page import Login_Class
from Page_object.Serach_User_Page import Search_User_Class
from Utilities import XLutilites
from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadConfigFile
#
#
# class Test_Search_User_Excel:
#     username = ReadConfigFile.GetUsername()
#     password = ReadConfigFile.GetPassword()
#     Log = Log_Class.log_generator()
#     Excel_file_Path = ".\\testCases\\TestData\\Test_Data.xlsx"
#
#     def test_SearchUser_Excel_006(self,setup):
#         self.driver = setup
#         self.lp = Login_Class(self.driver)
#         self.lp.Click_Login_Link()
#         self.lp.Enter_Username(self.username)
#         self.lp.Enter_Password(self.password)
#         self.lp.Click_Login_Button()
#
#         self.su = Search_User_Class(self.driver)
#         self.su.Click_Link_User_Management()
#         self.row_count = XLutilites.RowCount(self.Excel_file_Path,"SearchUser")
#         print("row_count -->" + str(self.row_count))
#         status_list = []
#         for r in range(2,self.row_count+1):
#             self.Search_Username = XLutilites.ReadData(self.Excel_file_Path,"SearchUser",r,2)
#             self.Expected_result = XLutilites.ReadData(self.Excel_file_Path,"SearchUser",r,3)
#             self.su.Click_Link_User_Management()
#             self.su.Enter_Username(self.Search_Username)
#             self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#
#             self.su.Click_SerachUser_Button()
#
#             if self.su.Validate_Search_User() == "pass" and self.Expected_result == "pass":
#                 actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
#                 Status = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "pass")
#                 status_list.append("pass")
#
#                 self.Log.info("test_search_user_006 is passed")
#                 self.driver.save_screenshot(".\\Screenshots\\test_search_user_006_Pass.png")
#                 self.Log.info("Testcase test_Login_006 is completed\n")
#                 # assert True
#
#             elif self.su.Validate_Search_User() == "pass" and self.Expected_result == "fail":
#                 actual_result = XLutilites.WriteData(self.Excel_file_Path,"SearchUser",r,4,"pass")
#                 Status = XLutilites.WriteData(self.Excel_file_Path,"SearchUser",r,5,"fail")
#                 status_list.append("fail")
#
#                 self.Log.info("test_search_user_006 is failed")
#                 self.driver.save_screenshot(".\\Screenshots\\test_search_user_006_Fail.png")
#                 self.Log.info("Testcase test_Login_006 is completed\n")
#                 # assert False
#
#             elif self.su.Validate_Search_User() == "fail" and self.Expected_result == "pass":
#                 actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
#                 Status = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "fail")
#                 status_list.append("fail")
#
#                 self.Log.info("test_search_user_006 is failed")
#                 self.driver.save_screenshot(".\\Screenshots\\test_search_user_006_Fail.png")
#                 self.Log.info("Testcase test_Login_006 is completed\n")
#                 # assert False
#             elif self.su.Validate_Search_User() == "fail" and self.Expected_result == "fail":
#                 actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
#                 Status = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "pass")
#                 status_list.append("pass")
#
#                 self.Log.info("test_search_user_006 is passed")
#                 self.driver.save_screenshot(".\\Screenshots\\test_search_user_006_Fail.png")
#                 self.Log.info("Testcase test_Login_006 is completed\n")
#                 # assert True
#
#         if "fail" not in status_list:
#             assert True
#         else:
#             assert False
#
import time

import pytest

# from Utilities import XLutilies
# from Utilities.readProperties import ReadConfigFile
# from pageObjects.Login_Page import Login_Class
# from pageObjects.Search_User_Page import Search_User_Class


class Test_Search_User_Excel:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()
    Excel_file_Path = ".\\testCases\\TestData\\Test_Data.xlsx"

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_Excel_006(self, setup):
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login_Button()
        self.su = Search_User_Class(self.driver)
        self.su.Click_Link_User_Management()
        self.row_count = XLutilites.RowCount(self.Excel_file_Path, "SearchUser")
        print("row count-->" + str(self.row_count))
        Stauts_List = []

        for r in range(2, self.row_count + 1):
            self.Search_Username = XLutilites.ReadData(self.Excel_file_Path, "SearchUser", r, 2)
            self.ExpectedResult = XLutilites.ReadData(self.Excel_file_Path, "SearchUser", r, 3)
            self.su.Click_Link_User_Management()
            self.su.Enter_Username(self.Search_Username)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(5)
            self.su.Click_SerachUser_Button()
            # time.sleep(5)
            if self.su.Validate_Search_User() == "pass" and self.ExpectedResult == "pass":
                actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
                Stauts = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "pass")
                Stauts_List.append("pass")
                # assert True
            elif self.su.Validate_Search_User() == "pass" and self.ExpectedResult == "fail":
                actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "pass")
                Stauts = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "fail")
                Stauts_List.append("fail")
                # assert False
            elif self.su.Validate_Search_User() == "fail" and self.ExpectedResult == "pass":
                actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
                Stauts = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "fail")
                Stauts_List.append("fail")
            # assert False
            elif self.su.Validate_Search_User() == "fail" and self.ExpectedResult == "fail":
                actual_result = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 4, "fail")
                Stauts = XLutilites.WriteData(self.Excel_file_Path, "SearchUser", r, 5, "pass")
                Stauts_List.append("pass")
                # assert True

        print("Testcase pass count-->" + str(Stauts_List.count("pass")))
        print("Testcase fail count-->" + str(Stauts_List.count("fail")))
        print(Stauts_List)
        if "fail" not in Stauts_List:
            assert True
        else:
            assert False

