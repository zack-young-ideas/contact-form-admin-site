"""
Defines tests run against the login page.
"""

from django.contrib.auth import get_user_model

from selenium.common import exceptions
from selenium.webdriver.common.by import By

from tests import base


User = get_user_model()


class LoginPageTest(base.BaseTestCase):

    def setUp(self):
        """
        Creates a new superuser to log in as.
        """
        self.admin_username = 'admin'
        self.admin_password = 'Lk54>4q5|Mk1'
        User.objects.create_superuser(
            self.admin_username,
            'admin@example.com',
            self.admin_password
        )
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

        username_field.send_keys(self.admin_username)
        password_field.send_keys(self.admin_password)
        submit_button.click()

        self.wait_for(lambda: self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/dashboard'
        ))

    def test_displays_error_message_if_login_fails(self):
        """
        Tests that an error message is displayed if login fails.
        """
        self.browser.get(self.live_server_url + '/login')

        self.assertEqual(self.browser.title, 'Login')

        # No error message is displayed initially.
        self.assertRaises(
            exceptions.NoSuchElementException,
            self.browser.find_element,
            By.ID,
            'error-message'
        )

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')
        submit_button = self.browser.find_element(By.NAME, 'submit')

        # If the user types an invalid username, ...
        username_field.send_keys('invalidUsername')
        password_field.send_keys(self.admin_password)
        submit_button.click()

        # an error message is displayed.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.ID, 'error-message').text,
            'Invalid username or password'
        ))

        # The user refreshes the page.
        self.browser.get(self.live_server_url + '/login')

        # No error message is displayed initially.
        self.assertRaises(
            exceptions.NoSuchElementException,
            self.browser.find_element,
            By.ID,
            'error-message'
        )

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')
        submit_button = self.browser.find_element(By.NAME, 'submit')

        # If the user types an invalid password, ...
        username_field.send_keys(self.admin_username)
        password_field.send_keys('invalidPassword')
        submit_button.click()

        # an error message is displayed.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.ID, 'error-message').text,
            'Invalid username or password'
        ))
