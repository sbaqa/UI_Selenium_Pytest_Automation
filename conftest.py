import os.path
import time
import pytest
import selenium
import logging as logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the pytest-html plugin to take and embed screenshot in html report, whenever test failed or xfailed.
    Detailed explanation could be found here https://www.youtube.com/watch?v=e6tL7IudnXY
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url("https://automationexercise.com"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in CLI --desktop-browser=Chrome or Firefox")
    parser.addoption('--host', default='staging',
                     help='host options: "staging", "production", or your own host for local testing')
    parser.addoption('--headless', default='true',
                     help='headless options: "true" or "false"')
    parser.addoption('--mobile-browser', default='brave',
                     help='option to define web or mobile browser')

@pytest.fixture(scope="class")
def login_test_setup(request):
    """
    Headless mode (default='true'): pytest -m tc2 --browser=chrome --headless=false
    Mobile/tablet screen size: pytest -m tc2 --browser=firefox --mobile-browser=firefox
    Desktop mode (default='chrome'): pytest -m tc2 --browser=firefox
    """
    global driver
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    mobile_browser = request.config.getoption("--mobile-browser")

    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        ch = Service(ChromeDriverManager().install())
        chrome_options = Options()

        if headless == "true":  # usage => pytest -m tc2 --browser=chrome --headless=true
            chrome_options.add_argument('--headless')  # type in CLI '--headless=false' to run test with visible UI
            logger.info(">>> Headless mode turned on <<<")

        driver = webdriver.Chrome(service=ch, options=chrome_options)
        driver.maximize_window()

        if mobile_browser == "chrome":
            driver.set_window_size(960, 640)
            size = driver.get_window_size()
            logger.info("Window size: width = {0}px, height = {1}px".format(size["width"], size["height"]))
            logger.info(">>> Tablet Chrome browser size set in CLI <<<")

    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        ff = Service(GeckoDriverManager().install())
        ff_options = Options()

        if headless == "true":
            ff_options.add_argument('--headless')
            logger.info(">>> Headless mode turned on <<<")

        driver = webdriver.Firefox(service=ff, options=ff_options)
        driver.maximize_window()

        # add both options => 'pytest -m tc2 --browser=firefox --mobile-browser=firefox'
        if mobile_browser == "firefox":
            driver.set_window_size(960, 640)
            size = driver.get_window_size()
            logger.info("Window size: width = {0}px, height = {1}px".format(size["width"], size["height"]))
            logger.info(">>> Tablet Firefox browser size set in CLI <<<")

    elif browser == "edge":
        from selenium.webdriver.edge.options import Options
        ed = Service(EdgeChromiumDriverManager().install())
        edge_options = Options()

        if headless == "true":
            edge_options.add_argument('--headless')
            logger.info(">>> Headless mode turned on <<<")

        driver = webdriver.Edge(service=ed, options=edge_options)
        driver.maximize_window()

        if mobile_browser == "edge":
            driver.set_window_size(960, 640)
            size = driver.get_window_size()
            logger.info("Window size: width = {0}px, height = {1}px".format(size["width"], size["height"]))
            logger.info(">>> Tablet Edge browser size set in CLI <<<")

    else:
        logger.info("Such browser is not supported, please contact QA Automation Team to learn more about the issue")

    driver.get(utils.URL)
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    logger.info("Test execution finished")
