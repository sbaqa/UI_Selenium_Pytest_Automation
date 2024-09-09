import pytest
from selenium.common import StaleElementReferenceException, NoSuchElementException
from configs.decorators import retry
from helpers.generic_helper import GenericHelpers
from pages.homePage import HomePage
from utils import utils as utils

@handle_exceptions(exceptions=(NoSuchElementException, StaleElementReferenceException))
@pytest.mark.regression
@pytest.mark.tc1
def test_register_user(login_test_setup):
    """ Test Case #1: New User Registration """

    # Verify that home page is visible and start signup
    login_actions = HomePage(login_test_setup).assert_home_page_visible()
    login_page = HomePage(login_test_setup).accept_cookies()
    login_page_asserts = login_page.click_topnav_signup_login_link()
    login_page_asserts.assert_login_page_is_visible()

    # Enter name and email address to continue signup
    rand_info = GenericHelpers(login_test_setup).generate_random_email_and_password()
    login_actions.fill_signup_form(rand_info['password'], rand_info['email'])

    # Verify that 'ENTER ACCOUNT INFORMATION' step is visible
    login_page_asserts.assert_signup_full_form_visible()
    login_actions.enter_account_information(utils.NAME, rand_info['password'])
    login_actions.fill_account_information()

    # check account was created
    login_page_asserts.assert_successfully_created_account(expected_title=utils.ACCOUNT_CREATED)

    # Delete account
    deleted_account_page = login_actions.delete_account()
    deleted_account_page.assert_account_deleted(expected_title=utils.DELETED_ACCOUNT_TITLE)
    home_page = deleted_account_page.click_continue_button()
    home_page.assert_home_page_visible()
