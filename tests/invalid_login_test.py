from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest
import pytest
import os
from ddt import ddt, data, unpack
from utilities.read_data import getCsvData


@pytest.mark.usefixtures("BrowserSetUp","GenerateEvidence")
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.loginPage = LoginPage(self.driver)

    @data(*getCsvData('C:\\Users\\malencar\\Documents\\MeusProjetos\\WebAutomation\\data\\invalid_login_test.csv'))
    @unpack
    def test_invalid_login(self, username, password):
        url = "https://the-internet.herokuapp.com/"
                
        self.loginPage.goToPage(url)
        self.loginPage.SelectFromLogin("loginForm")
        self.loginPage.Login(username, password)

        self.loginPage.markFinal("test_valid_login",not self.loginPage.IsLogged(), "Login was successfull")

        self.driver.quit()
