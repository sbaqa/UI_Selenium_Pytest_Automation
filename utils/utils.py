# Constants
import inspect

URL = "https://automationexercise.com"
INCORRECT_EMAIL = "test_user@test.com"
INCORRECT_PASSWORD = "admin123"
CORRECT_EMAIL = "user_test@test.com"
CORRECT_PASSWORD = "Formulaq1w2e3!"
LOGIN_FORM_HEADER = "Login to your account"
NAME = "test"
DATE = "5"
MONTH = "5"
YEAR = "1990"
ACCOUNT_CREATED = "ACCOUNT CREATED!"
TEST_USER_NAME = "testuser"
COOKIES_HEADER = "This site asks for consent to use your data"
DELETED_ACCOUNT_TITLE = "Account Deleted!"
HOME_PAGE_TITLE = "Automation Exercise"
NAVBAR_ACTIVE_LINK = "orange"
INCORRECT_EMAIL_ALERT = "Your email or password is incorrect!"

def whoami():
    return inspect.stack()[1][3]
