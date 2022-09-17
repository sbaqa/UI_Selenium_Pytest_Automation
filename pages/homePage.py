from helpers.generic_helper import GenericHelpers

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        self.visible_dashboard_id = "panel_draggable_1_0"
        self.dashboard_link_id = "menu_dashboard_index"

    def verify_home_page_visible(self):
        driver = self.driver
        GenericHelpers(driver).check_page_title("Automation Exercise")
        GenericHelpers(driver).check_active_link_navbar("orange")
