from selenium.webdriver.common.by import By
from locators.deleted_account_locators import DeletedAccountLocators
from pages.abstractPage import DefaultSeleniumDriver

d_a_locators = DeletedAccountLocators()

class DeletedAccount(DefaultSeleniumDriver):

    def click_continue_button(self):
        from pages.homePage import HomePage
        self.driver.find_element(By.XPATH, value=f"{d_a_locators.continue_button_xpath}").click()

        return HomePage(self.driver)

    def assert_account_deleted(self, expected_title: str):
        actual_title = self.driver.find_element(By.CSS_SELECTOR, value=f"{d_a_locators.deleted_account_title_css}").text
        assert actual_title == expected_title.upper(), (f"Found title '{actual_title}' does not "
                                                        f"equal expected '{expected_title}' title")
