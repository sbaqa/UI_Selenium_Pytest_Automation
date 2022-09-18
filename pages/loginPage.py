from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.login_signup_page_locators import LoginSignupLocators
from helpers.requests_helper import RequestsUtility

l_s_locators = LoginSignupLocators()

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.requests_helper = RequestsUtility()

    def click_topnav_signup_login_link(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.login_signup_topnav_link_xpath}").click()

    def get_email_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.email_address_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, l_s_locators.email_address_xpath)

    def get_password_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.password_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, l_s_locators.password_xpath)

    def get_name_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}")

    def get_signup_email_input(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}")
