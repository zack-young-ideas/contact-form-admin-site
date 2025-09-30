"""
Defines base test class used to launch browser window.
"""

import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


class BaseTestCase(StaticLiveServerTestCase):

    def setUp(self):
        """
        Opens Chrome.
        """
        self.startChrome()

    def tearDown(self):
        """
        Closes Chrome.
        """
        self.stopChrome()

    def startChrome(self):
        """
        Configures and launches an instance of Google Chrome.

        If the CHROME_BROWSER environment variable is set (to any
        value), a Chrome browser window will be opened and controlled
        by Selenium. The tests will be run against the site running in
        this browser window. If CHROME_BROWSER is not set, Chrome is
        run in headless mode (required when running tests on a CI server
        with no display).

        If the STAGING_SERVER environment variable is set to an IP
        address or domain name, the tests will be run against the
        server that resolves to that IP.
        """
        self.chrome_browser = os.environ.get('CHROME_BROWSER')
        self.browser_options = Options()
        if not self.chrome_browser:
            # If CHROME_BROWSER is not set, run Chrome in "headless"
            # mode.
            self.browser_options.add_argument('--headless')
        self.browser = webdriver.Chrome(
            options=self.browser_options
        )

    def stopChrome(self):
        """
        Closes the Chrome browser window.
        """
        self.browser.quit()

    def startFirefox(self):
        """
        Configures and launches an instance of Firefox.

        This is used in some tests to test cross-browser compatibility.
        """
        self.firefox_browser = os.environ.get('FIREFOX_BROWSER')
        self.firefox_browser_options = firefox_options.Options()
        self.firefox_browser_options.binary_location = os.environ.get(
            'FIREFOX_EXECUTABLE'
        )
        if not self.firefox_browser:
            # If FIREFOX_BROWSER is not set, run Firefox in "headless"
            # mode.
            self.firefox_browser_options.add_argument('--headless')
        self.firefox_browser = webdriver.Firefox(
            options=self.firefox_browser_options
        )

    def stopFirefox(self):
        """
        Closes the Firefox browser window.
        """
        self.firefox_browser.quit()

    def wait_for(self, fn, MAX_WAIT=5):
        """
        Used to wait until page elements are displayed.
        """
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
