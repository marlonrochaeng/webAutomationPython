import pytest
from werkzeug.security import safe_str_cmp
from selenium import webdriver

@pytest.yield_fixture(scope='function')
def BrowserSetUp(request, browser):
    print("Running browser setUp")
    if safe_str_cmp(browser,'firefox'):
        print("Tests will be executed on Firefox")
        driver = webdriver.Firefox()
    elif safe_str_cmp(browser,'chrome'):
        print("Tests will be executed on Chrome")
        driver = webdriver.Chrome("C:\\Users\\malencar\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)

    if request.cls:
        request.cls.driver = driver
    
    yield driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Operating system...")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")
