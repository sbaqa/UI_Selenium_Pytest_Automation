from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from helpers.generic_helper import GenericHelpers
from locators.login_signup_page_locators import LoginSignupLocators
from pages.abstractPage import DefaultSeleniumDriver
from utils import utils as utils


l_s_locators = LoginSignupLocators()

class LoginPage(DefaultSeleniumDriver):

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

    def assert_login_page_is_visible(self):

        # Check url is correct
        expected_url = f"{utils.URL}/login"
        found_url = self.driver.current_url
        assert expected_url == found_url, f"Found url => {found_url}, expected url => {expected_url}"

        # Check login page title detected
        self.verify_login_page_visible()

        # Check login form header is correct
        title = self.driver.find_element(By.XPATH, l_s_locators.login_header_xpath).text
        assert utils.login_form_header == title, f"ERROR! Found title => {title}"

    def verify_login_page_visible(self):
        GenericHelpers(self.driver).check_page_title("Signup / Login")

    def assert_signup_full_form_visible(self):
        form_title = self.driver.find_element(By.XPATH, l_s_locators.full_signup_form_xpath).is_displayed()
        assert form_title is True, f"ERROR! Actual boolean => {form_title}"

    def assert_incorrect_email_password_alert_shown(self, expected_alert_message: str):
        found_alert_message = self.driver.find_element(
            By.XPATH, value=f"{l_s_locators.incorrect_email_password_xpath % expected_alert_message}").text
        assert expected_alert_message == found_alert_message, f"Actual found message => {found_alert_message}, " \
                                                              f"expected alert message => {expected_alert_message}"

    def assert_successfully_created_account(self, expected_title: str):
        actual_title = self.driver.find_element(By.XPATH, value=f"{l_s_locators.account_created_header_xpath}").text
        assert expected_title == actual_title, f"Expected title => {expected_title}, but found => {actual_title}"
        self.driver.find_element(By.XPATH, value=f"{l_s_locators.registration_continue_button_xpath}").click()

    def assert_user_name_is_visible(self, user_name):
        user_name_button = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, f"{l_s_locators.user_name_navbar_xpath % user_name}")))
        assert user_name in user_name_button.text, f"Button was not visible and clickable, " \
                                                   f"so boolean => {user_name_button}, name => {user_name_button.text}"
        return user_name_button.text

    # def sign_in_with_empty_or_incorrect_credentials(self):
    #     """ Login with empty credentials, login with wrong credentials, verify flags were shown, user clicked on \
    #     'Forgot your password link' and was redirected to 'Reset Password' form """
    #     self.click_login_button()
    #     credentials_flag = self.driver.find_element(By.ID, self.invalid_credentials_flag_id).text
    #     logger.info("Credentials flag was fetched")
    #     if credentials_flag == utils.utils.expectedEmptyCredentialsFlag:
    #         assert len(credentials_flag) == 24, f"ERROR! Actual invalid credentials flag length" \
    #                                             f" => {len(credentials_flag)}"
    #         entered_credentials = self.login_crm_system("username", "password")
    #         if entered_credentials is not int:
    #             self.click_login_button()
    #             logger.info("Incorrect credentials entered")
    #             current_url = self.driver.current_url
    #             assert current_url == utils.utils.expectedInvalidCredentialsUrl, f"Url after wrong credentials " \
    #                                                                              f"is wrong, found {current_url}"
    #             invalid_credentials_flag = utils.utils.expectedInvalidCredentialsFlag
    #             if invalid_credentials_flag:
    #                 assert len(invalid_credentials_flag) == 19, f"ERROR! Actual invalid credentials flag length" \
    #                                                             f" => {len(invalid_credentials_flag)}"
    #                 self.click_forgot_password_link()
    #                 current_url = self.driver.current_url
    #                 assert current_url == utils.utils.forgotPasswordFormUrl, f"Url after click on 'forgot password'" \
    #                                                                          f" link is wrong, found {current_url}"
    #                 logger.info("'Forgot your password' link was clicked and user was redirected to 'Reset Password' form")
    #             else:
    #                 raise Exception("Flag for invalid credentials not found, please debug the issue")
    #
    #         else:
    #             raise Exception("Something wrong on with entered credentials, please debug the issue")
    #
    # def click_cancel_button_forgot_password_form(self):
    #     self.driver.find_element(By.XPATH, self.cancel_button_xpath).click()
    #
    # def cancel_fill_forgot_password_form(self, title):
    #     custom_page_title = self.driver.find_element(By.XPATH, self.title_name_xpath % title).text
    #     assert custom_page_title == utils.utils.forgotPasswordTitle, f"Actual found title => {custom_page_title}"
    #     self.click_cancel_button_forgot_password_form()
    #     current_redirection_url = self.driver.current_url
    #     assert current_redirection_url == utils.utils.cancelForgotPasswordUrl, f"Url after wrong credentials " \
    #                                                                      f"is wrong, found {current_redirection_url}"
    #
    # def fill_username_forgot_password_input(self, user):
    #     self.driver.find_element(By.NAME, self.security_user_name).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    #     self.driver.find_element(By.NAME, self.security_user_name).send_keys(user)
    #     logger.info("User filled 'Username' input")
    #
    # def click_reset_password_button(self):
    #     self.driver.find_element(By.XPATH, self.reset_password_btn_xpath).click()
    #     logger.info("User clicked 'Reset Password' button")
    #
    # def verify_banner_shown_and_closed(self):
    #     element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.contact_hr_xpath)))
    #     assert element.text == "Close", f"ERROR! Actual found text => {element.text}"
    #     element.click()
    #     logger.info("User closed 'Please contact HR...' banner")
    #     banner_elem = self.driver.find_element(By.XPATH, self.contact_hr_xpath).is_displayed()
    #     assert banner_elem is True, f"ERROR! Actual boolean => {banner_elem}"
    #
    # def fill_forgot_password_form(self, user):
    #     self.click_forgot_password_link()
    #     self.fill_username_forgot_password_input(user)
    #     self.click_reset_password_button()
    #     self.verify_banner_shown_and_closed()
