from selenium.webdriver.common.by import By
from utils import utils as utils
from helpers.generic_helpers import GenericHelpers

class LoginAsserts:

    def __init__(self, driver):
        self.driver = driver
        self.login_header_xpath = "//div[@class='login-form']/h2"
        self.full_signup_form_xpath = "//h2/b[text()='Enter Account Information']"

    def signup_login_page_check(self):

        # Check url is correct
        expected_url = f"{utils.URL}/login"
        found_url = self.driver.current_url
        assert expected_url == found_url, f"Found url => {found_url}, expected url => {expected_url}"

        # Check login page title detected
        self.verify_login_page_visible()

        # Check login form header is correct
        title = self.driver.find_element(By.XPATH, self.login_header_xpath).text
        assert utils.login_form_header == title, f"ERROR! Found title => {title}"

    def verify_login_page_visible(self):
        GenericHelpers(driver=self.driver).check_page_title("Signup / Login")

    def assert_signup_full_form_visible(self):
        form_title = self.driver.find_element(By.XPATH, self.full_signup_form_xpath).is_displayed()
        assert form_title is True, f"ERROR! Actual boolean => {form_title}"
