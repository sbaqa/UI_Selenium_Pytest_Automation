import time
from time import time
from selenium.webdriver.common.by import By
import logging as logger
import random
import string

class GenericHelpers:

    def __init__(self, driver):
        self.driver = driver
        self.link_style_color_xpath = "//a[contains(@style, 'color: orange;')]"

    def check_page_title(self, page_name):

        waiter = time() + 10
        while page_name not in self.driver.title and waiter > time():
            time.sleep(1)

        title = self.driver.title
        assert page_name in title, f"Expected {page_name} in {title}"

    def check_active_link_navbar(self, class_color):
        active_navbar_link = self.driver.find_element(By.XPATH, self.link_style_color_xpath).get_attribute('style')
        assert class_color in active_navbar_link, f"Expected color => {class_color}, found style attribute => " \
                                                  f"{active_navbar_link}"

    def generate_random_email_and_password(self, domain=None, email_prefix=None):
        logger.debug("Generating random email and password.")

        # Set domain and email prefix for email generation
        if not domain:
            domain = 'bordovski.pp.ua'
        if not email_prefix:
            email_prefix = 'testuser'

        # Set conditions for email generation
        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        email = email_prefix + '_' + random_string + '@' + domain

        # Set conditions for password generation
        password_length = 15
        password_string = ''.join(random.choices(string.ascii_letters, k=password_length))
        password = password_string + '2021' + '_for_' + email_prefix + '_' + random_string + '@' + domain

        # Dictionary for credentials
        random_info = {'email': email, 'password': password}
        logger.debug(f"Randomly generated email and password: {random_info}")

        return random_info

    def generate_random_integer(self):
        random_integer = int(random.randrange(500000000))
        return random_integer
