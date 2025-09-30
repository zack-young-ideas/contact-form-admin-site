"""
Defines tests run against the login page.
"""

from selenium.webdriver.common.by import By

from tests import base


class LoginPageTest(base.BaseTestCase):

    def setUp(self):
        """
        Creates a new superuser to log in as.
        """
        # Create superuser
        base.BaseTestCase.setUp(self)

    def test_can_login_successfully(self):
        """
        Tests that the superuser can log in successfully.
        """
        self.browser.get(self.live_server_url + '/login')

        self.assertEqual(self.browser.title, 'Login')

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')
        submit_button = self.browser.find_element(By.NAME, 'submit')

        username_field.send_keys('admin')
        password_field.send_keys('secretPassword')
        submit_button.click()

        self.wait_for(lambda: self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/dashboard'
        ))
