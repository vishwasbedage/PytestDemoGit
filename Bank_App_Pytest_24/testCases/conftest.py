import pytest
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://bankapp.credence.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(params=[

                ("Admin","pass"),
                ("Tushar","pass"),
                ("Admin420","fail"),
                ("demo2","pass"),
                ("demo","fail")
])
def getDataForSearchUser(request):
    return request.param



