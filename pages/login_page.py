from selenium.webdriver.common.by import By
from base.base_page import BasePage
from werkzeug.security import safe_str_cmp

class LoginPage(BasePage):
    #locators
    _login_field = (By.XPATH,"//input[@id='username']")
    _password_field = (By.XPATH,"//input[@id='password']")
    _login_button = (By.XPATH,"//i[contains(text(),'Login')]")
    _logout_button = (By.XPATH,"//i[@class='icon-2x icon-signout']")
    _login_message = (By.XPATH,"//div[@id='flash']")
    _select_login = (By.XPATH,"//a[@href='/login']")


    def __init__(self, driver):
        super().__init__(driver)
    
    def Login(self, username, password):
        self.SendKeys(self._login_field, username)
        self.SendKeys(self._password_field, password)
        self.ClickOn(self._login_button)
    
    def SelectFromLogin(self, menu_option):
        if safe_str_cmp(menu_option, "loginForm"):
            self.ClickOn(self._select_login)
        
    def IsLogged(self):
        message = self.WaitElement(locator=self._login_message,timeout=50)
        return "You logged into a secure area!" in message.text
    
    def goToPage(self, url):
        self.driver.get(url)
    