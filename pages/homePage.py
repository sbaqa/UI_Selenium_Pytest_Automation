from selenium.webdriver.common.by import By
from actions.login import LoginActions
from utils import utils as utils
from helpers.base_widget import Widget
from helpers.generic_helper import GenericHelpers
from pages.abstractPage import DefaultSeleniumDriver
from locators.home_page_locators import HomePageLocators
from pages.loginPage import LoginPage

h_p_locators = HomePageLocators()

class HomePage(DefaultSeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.widget = Widget(self.driver)
        self.gen_help = GenericHelpers(self.driver)

    def assert_home_page_visible(self):
        self.gen_help.check_page_title(utils.HOME_PAGE_TITLE)
        self.gen_help.check_active_link_navbar(utils.NAVBAR_ACTIVE_LINK)

        return LoginActions(self.driver)

    def click_accept_cookies_button(self):
        self.widget.wait_for_element_to_be_clickable(By.XPATH, h_p_locators.accept_cookies_button_xpath)
        self.driver.find_element(By.XPATH, h_p_locators.accept_cookies_button_xpath).click()

    def accept_cookies(self):
        self.widget.wait_for_text_to_be_present(locator_type=By.CSS_SELECTOR,
                                                locator_value=h_p_locators.cookies_title_header_css,
                                                text=utils.COOKIES_HEADER,
                                                timeout=15)
        self.click_accept_cookies_button()

        return LoginPage(self.driver)
