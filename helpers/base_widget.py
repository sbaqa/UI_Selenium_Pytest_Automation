from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.abstractPage import DefaultSeleniumDriver


class Widget(DefaultSeleniumDriver):

    def wait_for_element_to_be_clickable(self, locator_type, locator_value, timeout=30):
        locator = (locator_type, locator_value)

        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_text_to_be_present(self, locator_type, locator_value, text, timeout=30, poll_frequency=0.1):
        locator = (locator_type, locator_value)

        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            ec.text_to_be_present_in_element(locator, text),
            f'Timeout waiting for text "{text}" to be present in element located by {locator_type}="{locator_value}"'
        )
