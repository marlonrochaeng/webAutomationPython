import os
import unittest

import pytest
from ddt import data, ddt, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utilities.read_data import getCsvData

@pytest.mark.usefixtures("BrowserSetUp","GenerateEvidence")
@ddt
class LoginTest(unittest.TestCase):
    @pytest.yield_fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.loginPage = LoginPage(self.driver)
        yield
        self.driver.quit()

    @data(*getCsvData('data\\login\\invalid_login_test.csv'))
    @unpack
    def test_invalid_login(self, url, username, password):
        self.loginPage.goToPage(url)
        self.loginPage.SelectFromLogin("loginForm")
        self.loginPage.Login(username, password)
        self.loginPage.markFinal("test_valid_login",not self.loginPage.IsLogged(), "Login was successfull")
