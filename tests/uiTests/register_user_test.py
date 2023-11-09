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
@pytest.mark.regression
class TestRegisterUser:

    @pytest.fixture(autouse=True)  # https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request
    def class_tests_setup(self):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.login_actions = LoginActions(self.driver)
        self.login_page_asserts = LoginAsserts(self.driver)

    @pytest.mark.tc1
    def test_register_user(self):
        """ Test Case #1: New User Registration """

        try:
            # Verify that home page is visible successfully
            self.home_page.verify_home_page_visible()
            self.login_page.click_topnav_signup_login_link()
            self.login_page_asserts.signup_login_page_check()

            # Enter name and email address
            rand_info = GenericHelpers(self.driver).generate_random_email_and_password()
            self.login_actions.fill_signup_form(rand_info['password'], rand_info['email'])

            # Verify that 'ENTER ACCOUNT INFORMATION' is visible
            self.login_page_asserts.assert_signup_full_form_visible()
            self.login_actions.enter_account_information(utils.NAME, rand_info['password'])
            self.login_actions.fill_account_information()

            # close advertising popup
            self.login_page_asserts.successfully_created_account(utils.ACCOUNT_CREATED)

            # Delete account
            self.login_actions.delete_account()

        except (NoSuchElementException, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        except AttributeError as e:
            logger.error(">>> Searching element method may have an issue now or found data cannot be handled in "
                         "current test, so check the logs attentively please <<<")
            raise e
