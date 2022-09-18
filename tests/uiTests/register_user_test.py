import logging as logger
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from actions.login import LoginActions
from helpers.generic_helper import GenericHelpers
from utils import utils as utils

@pytest.mark.usefixtures("login_test_setup")
class TestRegisterUser:

    @pytest.mark.tc1
    def test_register_user(self):
        """ Test Case #1: New User Registration """

        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        login_actions = LoginActions(self.driver)
        login_page_asserts = LoginAsserts(self.driver)

        try:
            # Verify that home page is visible successfully
            home_page.verify_home_page_visible()
            login_page.click_topnav_signup_login_link()
            login_page_asserts.signup_login_page_check()

            # Enter name and email address
            rand_info = GenericHelpers(self.driver).generate_random_email_and_password()
            login_page.fill_signup_form(rand_info['password'], rand_info['email'])

            # Verify that 'ENTER ACCOUNT INFORMATION' is visible
            login_page_asserts.assert_signup_full_form_visible()
            login_actions.enter_account_information(utils.NAME, rand_info['password'])
            login_page.fill_account_information()
            login_page.successfully_created_account(utils.ACCOUNT_CREATED)

            # Delete account
            login_page.delete_account()

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
