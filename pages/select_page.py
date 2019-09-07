from selenium.webdriver.common.by import By
from base.base_page import BasePage
from werkzeug.security import safe_str_cmp

class SelectPage(BasePage):
    #locators
    _select_menu = "//select[@id='dropdown']"
    _dropdown = "//a[@href='/dropdown']"

    def __init__(self, driver):
        super().__init__(driver)
    
    def SelectFromLogin(self, menu_option):
        if safe_str_cmp(menu_option, "dropdown"):
            self.ClickOn("xpath", self._select_login)
    
    def Select(self, text):
        self.SelectElementByText('xpath',self._select_menu,text)
    
    def IsSelected(self,text):
        return safe_str_cmp(text,self.GetElement('xpath', self._select_menu).text)