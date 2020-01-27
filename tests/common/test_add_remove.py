import os
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.common import Common

@pytest.mark.usefixtures("BrowserSetUp")
class AddDelete(unittest.TestCase):
    @pytest.yield_fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.common = Common(self.driver)
        yield
        self.driver.quit()

    def test_add_delete(self):
        self.common.go_to("https://the-internet.herokuapp.com/add_remove_elements/")
        self.common.add_element()
        assert self.common.is_delete_displayed()
        self.common.remove_element()
        assert not self.common.is_delete_displayed()