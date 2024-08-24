
# 1 Configure interpreter
# 2 Check Terminal Setting :
# Setting--> Tools --> Terminal --> Shell Path  = "C:\Windows\system32\cmd.exe"

# 3 Set Default test runner to pytest
# Setting--> Tools --> Python integrated tool --> default test runner --> pytest

# 4 Install required libraries
# pip install selenium pytest pytest-xdist pytest-html allure-pytest

# 5 pytest rules
# python testcase file should start with "test_" or end with "_test"
# Class Name start with "Test"
# Method means testcases should start with "test_"


# 6 Test run commands

''''
Root folder but make sure your cmd is pointed at project
1 command --> pytest testCases/test_file1.py
using abs path --> command
2 command -- > pytest "D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jul 24\Pytest_Demo\testCases\test_file1.py"

pytest : it will search all the pytest file in folder and in folders also, this is  to run all testcases in project
3 command --> pytest

4 command --> pytest -v -s
verbose and std output for more detailing of test run

5 command -- > pytest -k "keyword"
e.g. --> pytest -k "sum"


6 For parallel run
command --> pytest -n=number
e.g. --> pytest -n=4
(n= no. of processor)


7: For grouping the test cases use –m
Command 
•	pytest –m “group_name”
•	pytest –m “group_name1 and group_name2”
•	pytest –m “group_name1 or group_name2


e.g. -- >
1. pytest -v -s -m  "regression"
2. pytest -v -s -m  "regression and sanity"
3. pytest -v -s -m  "regression or sanity"
4. ytest -v -s -m  "regression or sanity or group1"
5. pytest -v -s -m  "regression and sanity and group1"



8. command to ignore the warnings -->
pytest --disable-warnings


9. To generate html report
Command  pytest --html=myreport.html

e.g. -->
pytest --html=myreport.html -n=3
pytest --html=Reports/myreport.html -n=3  -m "group1"



10.	To generate  allure report
•	Command to generate the reports files  pytest -–alluredir=”Report_file_path”
•	Command to generate the allure reports  allure serve “Report_file_path”


'''
import pytest


class Test001:
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.group1

    def test_sum_001(self,demo_fixture):
        a= 10
        b = 20
        sum = a+b
        print("Sum of a + b",str(sum))
        if sum == 30:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.group2

    def test_mul_002(self,demo_fixture):
        a = 2
        b = 2
        mul = a * b
        print("Mul of a * b =" + str(mul))
        if mul == 5:
            assert True
        else:
            assert False

    @pytest.mark.regression
    @pytest.mark.group1
    def sub_003(self,demo_fixture):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_sub_004(self,demo_fixture):
        a = 20
        b = 2
        sub = a - b
        print("sub of a - b =" + str(sub))
        if sub == 18:
            assert True
        else:
            assert False











