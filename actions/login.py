import time
import random
import string
import logging as logger
from utils import utils as utils
from selenium.webdriver.common.by import By
from asserts.login_page_asserts import LoginAsserts
from locators.login_signup_page_locators import LoginSignupLocators
from helpers.requests_helper import RequestsUtility
from pages.loginPage import LoginPage

l_s_locators = LoginSignupLocators()

class LoginActions:

    def __init__(self, driver):
        self.driver = driver
        self.requests_helper = RequestsUtility()
        self.login_page = LoginPage(self.driver)
        self.login_page_asserts = LoginAsserts(self.driver)

    def fill_credentials(self, username, password):
        self.login_page.get_email_input().send_keys(username)
        self.login_page.get_password_input().send_keys(password)
        self.click_login_button()

    def click_login_button(self):
        self.driver.find_element(By.XPATH, l_s_locators.login_button_xpath).click()
        time.sleep(3)

    def enter_account_information(self, set_name, set_password):
        self.click_signup_title_radio_button()
        self.set_name_and_password(set_name, set_password)
        self.set_date_of_birth()
        self.set_newsletter_offers_checkboxes()

    def fill_signup_form(self, name, email):
        self.login_page.get_name_input().send_keys(name)
        self.login_page.get_signup_email_input().send_keys(email)
        self.click_signup_button()

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_button_xpath}").click()

    def click_signup_title_radio_button(self):
        """ Set Mr./Mrs. title in 'ENTER ACCOUNT INFORMATION' block """
        self.driver.find_element(By.ID, value=f"{l_s_locators.title_radio_button_id}").click()

    def set_name_and_password(self, name, password):
        """ Set name and set password in 'ENTER ACCOUNT INFORMATION' block """
        name_field = self.driver.find_element(By.ID, value=f"{l_s_locators.input_name_field_id}")
        password_field = self.driver.find_element(By.ID, value=f"{l_s_locators.input_password_field_id}")
        return name_field.send_keys(name), password_field.send_keys(password)

    def set_date_of_birth(self):
        """ Set date of birth in 'ENTER ACCOUNT INFORMATION' block """

        # set date
        self.driver.find_element(By.ID, value=f"{l_s_locators.select_dd_date_id}").click()
        days_list = self.driver.find_elements(By.XPATH, value=f"{l_s_locators.days_xpath}")
        chosen_day = random.choice(days_list)
        chosen_day.click()

        # set month
        self.driver.find_element(By.ID, value=f"{l_s_locators.select_dd_month_id}").click()
        months_list = self.driver.find_elements(By.XPATH, value=f"{l_s_locators.months_xpath}")
        chosen_month = random.choice(months_list)
        chosen_month.click()

        # set year
        self.driver.find_element(By.ID, value=f"{l_s_locators.select_dd_year_id}").click()
        years_list = self.driver.find_elements(By.XPATH, value=f"{l_s_locators.years_xpath}")
        chosen_year = random.choice(years_list)
        chosen_year.click()

    def set_newsletter_offers_checkboxes(self):
        """ Check "signup for newsletter" and "receive special offers" checkboxes """
        self.driver.find_element(By.ID, value=f"{l_s_locators.newsletter_checkbox_id}").click()
        self.driver.find_element(By.ID, value=f"{l_s_locators.special_offers_checkbox_id}").click()

    def fill_account_information(self):
        """ Fill 'ACCOUNT INFORMATION' block """
        ai_inputs_list = self.driver.find_elements(By.XPATH,
                                                   value=f"{l_s_locators.address_information_value_xpath}/input")
        for field in ai_inputs_list:

            if field.get_attribute("id") == "mobile_number" or field.get_attribute("id") == "zipcode":
                input_value = int(''.join(random.choices(string.digits, k=10)))
                logger.info(f"Generated input integer ===> : {input_value}")
                assert len(str(input_value)) == 10, f"Actual found value length => {len(str(input_value))}"
                field.send_keys(input_value)

            else:
                input_value = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))
                logger.info(f"Generated input string ===> : {input_value}")
                field.send_keys(input_value)
                assert len(input_value) == 10, f"Actual found value length => {len(input_value)}"

        # Open 'country' dropdown, check if all options visible, select any option and click on it
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.address_information_value_xpath}/select").click()
        country_options = self.driver.find_elements(By.XPATH,
                                                    value=f"{l_s_locators.address_information_value_xpath}//option")
        for option in country_options:
            assert option.is_displayed() is True, f"Option was not found so boolean is {option.is_displayed()}"
        chosen_option = random.choice(country_options)
        chosen_option.click()

        # Click create account button
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.create_account_button_xpath}").click()

    def delete_account(self):
        email = self.login_page_asserts.user_name_is_visible(utils.TEST_USER_NAME)
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.delete_account_button_xpath}").click()

        payload = {
            "email": email
        }

        self.requests_helper.delete(f"deleteAccount", body_params=payload, expected_status_code=200)

    def click_logout_navbar(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.logout_button_xpath}").click()
