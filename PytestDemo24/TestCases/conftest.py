import pytest


@pytest.fixture()
def demo_fixture():       ### browser invoke
    print("Test runner started --> this code is fixture")    ## broser open chrome
    yield
    print("test run ended --> this is fixture")     ## browser close

