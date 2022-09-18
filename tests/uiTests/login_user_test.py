import pytest
import logging as logger
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from asserts.login_page_asserts import LoginAsserts
from tc_params.login_params import second_tc_login_params
from pages.loginPage import LoginPage
from actions.login import LoginActions
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("login_test_setup")
class TestLoginPage:

    @pytest.mark.tc2
    @pytest.mark.parametrize("email, password", second_tc_login_params())
    def test_login_user_correct_email_and_password(self, email, password):
        """Test Case #2: click on 'login/signup' button in navbar, fill form and delete account"""

        login_page = LoginPage(self.driver)
        login_actions = LoginActions(self.driver)
        home_page = HomePage(self.driver)
        login_page_asserts = LoginAsserts(self.driver)

        try:
            # Verify that home page is visible successfully
            home_page.verify_home_page_visible()

            # click Signup/Login link and verify 'Login to your account' is visible
            home_page.verify_home_page_visible()
            login_page.click_topnav_signup_login_link()
            login_page_asserts.signup_login_page_check()

            # fill form and click login
            login_actions.fill_credentials(email, password)

            # Verify that 'Logged in as username' is visible and delete account
            login_page_asserts.user_name_is_visible(utils.NAME)

            # Not relevant step => delete account which is not needed for happy pass in this test case
            # login_page.delete_account()

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")

    @pytest.mark.tc3
    def test_login_user_with_incorrect_email_and_password(self):
        """Test Case #3: login with incorrect email and password"""

        login_page = LoginPage(self.driver)
        login_actions = LoginActions(self.driver)
        login_page_asserts = LoginAsserts(self.driver)

        try:
            # Sign in and check alert message show up
            login_page.click_topnav_signup_login_link()
            login_page_asserts.signup_login_page_check()
            login_actions.fill_credentials(utils.INCORRECT_EMAIL, utils.INCORRECT_PASSWORD)
            login_page_asserts.incorrect_email_password_alert_shown("Your email or password is incorrect!")

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            self.driver.refresh()
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")

    @pytest.mark.tc4
    def test_logout_user(self):
        """Test Case #4: logout user with correct credentials"""

        login_page = LoginPage(self.driver)
        login_actions = LoginActions(self.driver)
        home_page = HomePage(self.driver)
        login_page_asserts = LoginAsserts(self.driver)

        try:
            # Verify that home page is visible successfully
            home_page.verify_home_page_visible()

            # click Signup/Login link and verify 'Login to your account' is visible
            home_page.verify_home_page_visible()
            login_page.click_topnav_signup_login_link()
            login_page_asserts.signup_login_page_check()

            # fill form and click login
            login_actions.fill_credentials(utils.CORRECT_EMAIL, utils.CORRECT_PASSWORD)

            # Verify that 'Logged in as username' is visible and delete account
            login_page_asserts.user_name_is_visible(utils.NAME)

            # Click logout and verify user is navigated to login page
            login_actions.click_logout_navbar()
            login_page_asserts.verify_login_page_visible()

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
