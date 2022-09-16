import time
from selenium.webdriver.common.by import By
from locators.login_signup_page_locators import LoginSignupLocators
from helpers.requests_helper import RequestsUtility
from pages.loginPage import LoginPage

l_s_locators = LoginSignupLocators()

class LoginActions:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def fill_credentials(self, username, password):
        self.login_page.get_email().send_keys(username)
        self.login_page.get_password().send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, l_s_locators.login_button_xpath).click()
        time.sleep(3)

    def enter_account_information(self, set_name, set_password):
        self.login_page.click_signup_title_radio_button()
        self.login_page.set_name_and_password(set_name, set_password)
        self.login_page.set_date_of_birth()
        self.login_page.set_newsletter_offers_checkboxes()
