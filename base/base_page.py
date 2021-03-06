from selenium.webdriver.common.by import By
from werkzeug.security import safe_str_cmp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from traceback import print_stack
import logging
import utilities.custom_logger as cl
import time
import os
import pytest


class BasePage():

    log = cl.CustomLogger()

    def __init__(self, driver):
        self.driver = driver
        self.resultList = []

    def takeScreenshot(self, resultMessage):
        folderName = str(pytest.time_start)+'/'+os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].split('___')[0]+'/'
        pytest.screenshotDirectory = os.path.join('screenshots/' ,folderName)
        fileName = resultMessage.replace(' ','_') + '_' + str(round(time.time() * 1000)) + '.png'
        finalFile = pytest.screenshotDirectory + fileName
        try:
            if not os.path.exists(pytest.screenshotDirectory):
                os.makedirs(pytest.screenshotDirectory)
            self.driver.save_screenshot(finalFile)
            self.log.info("Screenshot saved to: "+finalFile)
        except:
            self.log.error("### Exception Ocurred")
            print_stack()

    def go_to(self, url):
        self.driver.get(url)

    def GetElement(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info("Element found...")
        except:
            self.log.info("Element not found...")
            raise
        return element

    def GetElements(self, locator):
        
        elements = self.driver.find_elements(*locator)
        if len(elements) > 0:
            self.log.info("Element found...")
            return True
        else:
            self.log.info("Element not found...")
            return False
            

    def ClickOn(self, locator):
        try:
            element = self.GetElement(locator)
            element.click()
            self.log.info("Clicked on : "+str(locator[1]))
        except:
            self.log.info("Could not click on element: "+str(locator[1]))
            print_stack()
            raise
    
    def SendKeys(self, locator, text=""):
        try:
            element = self.GetElement(locator)
            element.send_keys(text)
            self.log.info("Keys sended to: " +str(locator[1]))
        except:
            self.log.info("Could not send keys to element: "+str(locator[1]))
            print_stack()
            raise

    def SelectElementByText(self, locator, text=""):
        try:
            element = self.GetElement(locator)
            select = Select(element)
            select.select_by_visible_text(text)
            self.log.info("Selected element from menu: "+str(locator[1]))
        except:
            self.log.info("Could not select element: "+str(locator[1]))
            print_stack()
            raise

    def IsElementPresent(self, locator):
        try:
            element = self.GetElement(locator)
            if element:
                self.log.info("Element found...")
                return True
            else:
                self.log.info("Element not found...")
                return False
        except:
            self.log.info("Element not found...")
            return False

    def WaitElement(self, locator, timeout=20):
        element = None
        try:
            self.log.info("Waiting for :: " + str(timeout) + " :: seconds for element")
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except:
            self.log.info("Element not found: "+str(locator[1]))
            print_stack()
        return element

    def get_element_size(self, locator):
        el = self.GetElement(locator)
        return el.size

    def get_element_attribute(self, locator, attribute):
        el = self.GetElement(locator)
        return el.get_attribute(attribute)

    def setResult(self, result, resultMessage):
        self.takeScreenshot(resultMessage)
        try:
            if result:
                self.resultList.append("PASS")
                self.log.info("### VERIFICATION SUCCESSFULL:: "+ resultMessage)

            else:
                self.resultList.append("FAIL")
                self.log.info("### VERIFICATION FAILED:: "+ resultMessage)  
        except:
            self.resultList.append("FAIL")
            self.log.info("### EXCEPTION OCCURRED:: "+ resultMessage)  
    
    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " ###TEST FAILED...")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ###TEST SUCCESSFUL...")
            self.resultList.clear()
            assert True == True
