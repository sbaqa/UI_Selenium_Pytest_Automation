from selenium.webdriver.common.by import By
import logging as logger


class ActionsHelper:

    def __init__(self, driver):
        self.driver = driver

    def get_input(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            logger.info("Locator type " , locatorType , " not correct/supported")
        return False

    def get_element(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            logger.info("Element Found with locator: " , locator , " and locatorType: " , locatorType)
        except:
            logger.info("Element not found with locator: " , locator , " and  locatorType: " , locatorType)
        return element
