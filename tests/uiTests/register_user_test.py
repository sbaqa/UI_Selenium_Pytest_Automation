import logging as logger
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from asserts.login_page_asserts import LoginAsserts
from pages.abstractPage import DefaultSeleniumDriver
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from actions.login import LoginActions
from helpers.generic_helper import GenericHelpers
from utils import utils as utils

@pytest.mark.regression
@pytest.mark.tc1
def test_register_user(login_test_setup):
    """ Test Case #1: New User Registration """

    try:
        # Verify that home page is visible successfully
        login_actions = HomePage(login_test_setup).verify_home_page_visible()
        login_page = HomePage(login_test_setup).accept_cookies()
        login_page_asserts = login_page.click_topnav_signup_login_link()
        login_page_asserts.signup_login_page_check()

        # Enter name and email address
        rand_info = GenericHelpers(login_test_setup).generate_random_email_and_password()
        login_actions.fill_signup_form(rand_info['password'], rand_info['email'])

        # Verify that 'ENTER ACCOUNT INFORMATION' is visible
        login_page_asserts.assert_signup_full_form_visible()
        login_actions.enter_account_information(utils.NAME, rand_info['password'])
        login_actions.fill_account_information()

        # close advertising popup
        login_page_asserts.successfully_created_account(expected_title=utils.ACCOUNT_CREATED)

        # Delete account
        deleted_account_page = login_actions.delete_account()
        deleted_account_page.assert_account_deleted(expected_title=utils.DELETED_ACCOUNT_TITLE)
        # TODO => add click on continue button and verify it was redirected to sign in button
        # TODO => try/except fix

    except (NoSuchElementException, StaleElementReferenceException) as e:
        logger.error("Locator issue, maybe it was not shown or found by driver")
        raise e

    except AttributeError as e:
        logger.error(">>> Searching element method may have an issue now or found data cannot be handled in "
                     "current test, so check the logs attentively please <<<")
        raise e
