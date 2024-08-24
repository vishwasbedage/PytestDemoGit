import selenium.webdriver.chrome.webdriver
from selenium import webdriver
import pytest

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     # webdriver.Chrome(options=chrome_options)
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     return driver

## we need to add command liner (--browser)
def pytest_addoption(parser):
    parser.addoption("--browser")

# Pytest fixture for setting up the WebDriver based on the selected browser
@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")  # Retrieve the browser option from command line
    if browser == "chrome":  # Check if the selected browser is Chrome
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    elif browser == "firefox":  # Check if the selected browser is Firefox
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()  # Initialize Firefox WebDriver
    elif browser == "edge":  # Check if the selected browser is Edge
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()  # Initialize Edge WebDriver
    else:  # Default to headless Chrome if no browser is specified or recognized
        print("Test Run - Headless")
        driver = webdriver.Chrome(options=chrome_options)  # Initialize headless Chrome WebDriver
    driver.maximize_window()  # Maximize the browser window
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Navigate to the login page
    yield driver  # Yield the WebDriver instance to be used in tests
    driver.quit()  # Quit the WebDriver after the test is completed


@pytest.fixture(params=[

    ("Admin","admin123","Login_Pass"),
    ("Admin","admin1234","Login_Fail"),
    ("Admin1","admin123","Login_Fail"),
    ("Admin1","admin1234","Login_Fail")
])
def getDataForLogin(request):
    return request.param



