import os
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.common import Common

@pytest.mark.usefixtures("BrowserSetUp")
class BrokenImages(unittest.TestCase):
    @pytest.yield_fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.common = Common(self.driver)
        yield
        self.driver.quit()

    def test_broken_images(self):
        self.common.go_to("https://the-internet.herokuapp.com/broken_images")
        assert self.common.is_image_broken()