"""
Defines tests run against the login page.
"""

from django.contrib.auth import get_user_model

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
