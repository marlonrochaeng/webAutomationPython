from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.select_page import SelectPage
import unittest
import pytest
import os
from ddt import ddt, data, unpack
from utilities.read_data import getCsvData


@pytest.mark.usefixtures("BrowserSetUp","GenerateEvidence")
@ddt
class SelectTest(unittest.TestCase):

    @pytest.yield_fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.selectPage = SelectPage(self.driver)
        yield
        self.driver.quit()

    def test_valid_login(self, username, password):
        url = "https://the-internet.herokuapp.com/"
                
        self.selectPage.goToPage(url)
        self.selectPage.SelectFromLogin("dropdown")
        self.selectPage.markFinal("test_valid_login",self.selectPage.IsSelected(), "Select is ok...")
