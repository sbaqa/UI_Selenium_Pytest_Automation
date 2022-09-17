import random
import string
import time
from utils import utils as utils
import logging as logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def get_email(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.email_address_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, l_s_locators.email_address_xpath)

    def get_password(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.password_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        return self.driver.find_element(By.XPATH, l_s_locators.password_xpath)

    def incorrect_email_password_alert_shown(self, expected_alert_message: str):
        found_alert_message = self.driver.find_element(
            By.XPATH, value=f"{l_s_locators.incorrect_email_password_xpath % expected_alert_message}").text
        assert expected_alert_message == found_alert_message, f"Actual found message => {found_alert_message}, " \
                                                              f"expected alert message => {expected_alert_message}"

    def fill_signup_form(self, name, email):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.name_xpath}").send_keys(name)
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}").send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.signup_email_xpath}").send_keys(email)
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
        ai_inputs_list = self.driver.find_elements(By.XPATH, value=f"{l_s_locators.address_information_value_xpath}/input")
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

        # Open 'country' dd, check if all options visible, select any option and click on it
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.address_information_value_xpath}/select").click()
        country_options = self.driver.find_elements(By.XPATH, value=f"{l_s_locators.address_information_value_xpath}//option")
        for option in country_options:
            assert option.is_displayed() is True, f"Option was not found so boolean is {option.is_displayed()}"
        chosen_option = random.choice(country_options)
        chosen_option.click()

        # Click create account button
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.create_account_button_xpath}").click()

    def successfully_created_account(self, expected_title: str):
        actual_title = self.driver.find_element(By.XPATH, value=f"{l_s_locators.account_created_header_xpath}").text
        assert expected_title == actual_title, f"Expected title => {expected_title}, but found => {actual_title}"
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.registration_continue_button_xpath}").click()

    def user_name_is_visible(self, user_name):
        user_name_button = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"{l_s_locators.user_name_navbar_xpath % user_name}")))
        assert user_name in user_name_button.text, f"Button was not visible and clickable, " \
                                                   f"so boolean => {user_name_button}, name => {user_name_button.text}"
        return user_name_button.text

    def delete_account(self):
        email = self.user_name_is_visible(utils.TEST_USER_NAME)
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.delete_account_button_xpath}").click()

        payload = {
            "email": email
        }

        self.requests_helper.delete(f"deleteAccount", body_params=payload, expected_status_code=200)

    def click_logout_navbar(self):
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.logout_button_xpath}").click()
