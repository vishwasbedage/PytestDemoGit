pytest -v -s -n=2 -m "sanity" --html=HTML_Reports/myreport.html --alluredir="AllureReports" --disable-warnings --browser chrome
allure serve "AllureReports"