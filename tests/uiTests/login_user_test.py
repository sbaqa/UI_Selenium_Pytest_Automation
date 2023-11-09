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
@pytest.mark.regression
class TestLoginPage:

    @pytest.fixture(autouse=True)  # https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request
    def class_tests_setup(self):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.login_actions = LoginActions(self.driver)
        self.login_page_asserts = LoginAsserts(self.driver)

    @pytest.mark.tc2
    @pytest.mark.parametrize("email, password", [
        ("user_test@test.com", "Formulaq1w2e3!"),
        pytest.param("random_username", "admin123",
                     marks=pytest.mark.xfail(reason="Non-existing username entered")),
        pytest.param(" ", " ",
                     marks=pytest.mark.xfail(reason="Empty credentials")),
        pytest.param("111@", "qwertyADMIN",
                     marks=pytest.mark.xfail(reason="Wrong credentials")),
        pytest.param(" ", "admin123",
                     marks=pytest.mark.xfail(reason="Empty username")),
        pytest.param("Admin", " ",
                     marks=pytest.mark.xfail(reason="Empty password"))
    ])
    def test_login_user_correct_email_and_password(self, email, password):
        """Test Case #2: click on 'login/signup' button in navbar, fill form and delete account"""

        try:
            # Verify that home page is visible successfully
            self.home_page.verify_home_page_visible()

            # click Signup/Login link and verify 'Login to your account' is visible
            self.home_page.verify_home_page_visible()
            self.login_page.click_topnav_signup_login_link()
            self.login_page_asserts.signup_login_page_check()

            # fill form and click login
            self.login_actions.fill_credentials(email, password)

            # Verify that 'Logged in as username' is visible and delete account
            self.login_page_asserts.user_name_is_visible(utils.NAME)

            # Not relevant step => delete account which is not needed for happy pass in this test case
            # login_page.delete_account()

        except (NoSuchElementException, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        except AttributeError as e:
            logger.error(">>> Searching element method may have an issue now or found data cannot be handled in "
                         "current test, so check the logs attentively please <<<")
            raise e

    @pytest.mark.tc3
    def test_login_user_with_incorrect_email_and_password(self):
        """Test Case #3: login with incorrect email and password"""

        try:
            # Sign in and check alert message show up
            self.login_page.click_topnav_signup_login_link()
            self.login_page_asserts.signup_login_page_check()
            self.login_actions.fill_credentials(utils.INCORRECT_EMAIL, utils.INCORRECT_PASSWORD)
            self.login_page_asserts.incorrect_email_password_alert_shown("Your email or password is incorrect!")

        except (NoSuchElementException, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        except AttributeError as e:
            logger.error(">>> Searching element method may have an issue now or found data cannot be handled in "
                         "current test, so check the logs attentively please <<<")
            raise e

    @pytest.mark.tc4
    def test_logout_user(self):
        """Test Case #4: logout user with correct credentials"""

        try:
            # Verify that home page is visible successfully
            self.home_page.verify_home_page_visible()

            # click Signup/Login link and verify 'Login to your account' is visible
            self.home_page.verify_home_page_visible()
            self.login_page.click_topnav_signup_login_link()
            self.login_page_asserts.signup_login_page_check()

            # fill form and click login
            self.login_actions.fill_credentials(utils.CORRECT_EMAIL, utils.CORRECT_PASSWORD)

            # Verify that 'Logged in as username' is visible and delete account
            self.login_page_asserts.user_name_is_visible(utils.NAME)

            # Click logout and verify user is navigated to login page
            self.login_actions.click_logout_navbar()
            self.login_page_asserts.verify_login_page_visible()

        except (NoSuchElementException, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        except AttributeError as e:
            logger.error(">>> Searching element method may have an issue now or found data cannot be handled in "
                         "current test, so check the logs attentively please <<<")
            raise e
