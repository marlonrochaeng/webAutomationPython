from selenium.webdriver.common.by import By
from base.base_page import BasePage
from werkzeug.security import safe_str_cmp
import requests

class Common(BasePage):
    #add/remove elements
    _add_element = (By.XPATH,"//button[contains(text(),'Add Element')]")
    _delete_element = (By.XPATH,"//button[contains(text(),'Delete')]")

    #verify images
    _images = ['asdf.jpg', 'hjkl.jpg', 'img/avatar-blank.jpg']

    #checkboxes
    _checkbox1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
    _checkbox2 = (By.XPATH, "(//input[@type='checkbox'])[2]")


    def __init__(self, driver):
        super().__init__(driver)

    #add/remove elements
    
    def add_element(self):
        self.ClickOn(self._add_element)

    def remove_element(self):
        self.ClickOn(self._delete_element)

    def is_delete_displayed(self):
        return self.IsElementPresent(self._delete_element)

    #verify images

    def is_image_broken(self):
        result = []
        for i in self._images:
            response = requests.get("https://the-internet.herokuapp.com/"+i)
            result.append(response.status_code)
        return 404 in result

    def click_and_check(self):
        self.ClickOn(self._checkbox1)
        result1 = self.get_element_attribute(self._checkbox1, "checked")
        self.ClickOn(self._checkbox2)
        result2 = self.get_element_attribute(self._checkbox2, "checked")
        return result1 and not result2