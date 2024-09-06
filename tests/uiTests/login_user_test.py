import pytest
from pages.homePage import HomePage
from utils import utils as utils


pytestmark = [pytest.mark.regression]

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
def test_login_user_correct_email_and_password(login_test_setup, email, password):
    """ Test Case #2: click on 'login/signup' button in navbar, fill form and delete account """

    # Verify that home page is visible successfully
    login_actions = HomePage(login_test_setup).assert_home_page_visible()
    login_page = HomePage(login_test_setup).accept_cookies()

    # click Signup/Login link and verify 'Login to your account' is visible
    login_actions.click_topnav_signup_login_link()
    login_page.assert_login_page_is_visible()

    # fill form and click login
    login_actions.fill_credentials(email, password)

    # Verify that 'Logged in as username' is visible and delete account
    login_page.assert_user_name_is_visible(utils.NAME)


@pytest.mark.tc3
def test_login_user_with_incorrect_email_and_password(login_test_setup):
    """ Test Case #3: login with incorrect email and password """

    # Sign in and check alert message show up
    login_actions = HomePage(login_test_setup).assert_home_page_visible()
    login_page = HomePage(login_test_setup).accept_cookies()

    # click Signup/Login link and verify 'Login to your account' text is visible
    login_actions.click_topnav_signup_login_link()
    login_page.assert_login_page_is_visible()
    login_actions.fill_credentials(utils.INCORRECT_EMAIL, utils.INCORRECT_PASSWORD)
    login_page.assert_incorrect_email_password_alert_shown(utils.INCORRECT_EMAIL_ALERT)

@pytest.mark.tc4
def test_logout_user(login_test_setup):
    """Test Case #4: logout user with correct credentials"""

    # Sign in and check alert message show up
    login_actions = HomePage(login_test_setup).assert_home_page_visible()
    login_page = HomePage(login_test_setup).accept_cookies()

    # click Signup/Login link and verify 'Login to your account' is visible
    login_actions.click_topnav_signup_login_link()
    login_page.assert_login_page_is_visible()

    # fill form and click login
    login_actions.fill_credentials(utils.CORRECT_EMAIL, utils.CORRECT_PASSWORD)

    # Verify that 'Logged in as username' is visible
    login_page.assert_user_name_is_visible(utils.NAME)

    # Click logout and verify user is navigated to login page
    login_actions.click_logout_navbar()
    login_page.verify_login_page_visible()
