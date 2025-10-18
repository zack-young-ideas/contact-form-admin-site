"""
Defines tests run against the admin dashboard page.
"""

from django.contrib.auth import get_user_model

from selenium.webdriver.common.by import By

from tests import base


User = get_user_model()


class DashboardPageTest(base.BaseTestCase):

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

    def test_must_be_authenticated_in_to_view(self):
        """
        GET requests return 404 if not authenticated.
        """
        self.browser.get(self.live_server_url + '/dashboard')

        self.assertEqual('404 - Not Found', self.browser.title)
        self.assertIn('Page Not Found', self.browser.page_source)

    def test_can_log_out_successfully(self):
        """
        Tests that an admin user can log out successfully.
        """
        self.browser.get(self.live_server_url + '/login')

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

        # The user must close the modal window first.
        modal_window = self.browser.find_element(By.ID, 'prompt-window')
        self.wait_for(lambda: self.assertTrue(
            modal_window.is_displayed()
        ))

        cancel_buttons = modal_window.find_elements(
            By.CLASS_NAME,
            'close-modal-button'
        )
        cancel_buttons[0].click()

        self.wait_for(lambda: self.assertFalse(
            modal_window.is_displayed()
        ))

        # The user clicks the "Logout" button.
        logout_button = self.browser.find_element(By.LINK_TEXT, 'Logout')
        logout_button.click()

        self.wait_for(lambda: self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/login'
        ))

    def test_user_is_prompted_to_enable_two_factor_authentication(self):
        """
        Users are prompted to enable two-factor authentication.

        Any time a user logs in, if they have not yet enabled two-factor
        authentication, a modal window appears prompting them to set
        it up.
        """
        self.browser.get(self.live_server_url + '/login')

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

        modal_window = self.browser.find_element(By.ID, 'prompt-window')
        self.wait_for(lambda: self.assertTrue(
            modal_window.is_displayed()
        ))

        # The user clicks the button labeled 'Enable Now'.
        enable_button = modal_window.find_element(
            By.LINK_TEXT,
            'Enable Now'
        )
        enable_button.click()

        self.wait_for(lambda: self.assertEqual(
            self.browser.current_url,
            self.live_server_url + '/dashboard/two-factor-auth'
        ))

    def test_users_can_close_modal_window(self):
        """
        Users can close the modal window prompting them to enable 2FA.
        """
        self.browser.get(self.live_server_url + '/login')

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

        modal_window = self.browser.find_element(By.ID, 'prompt-window')
        self.wait_for(lambda: self.assertTrue(
            modal_window.is_displayed()
        ))

        # The user clicks the button labeled 'X'.
        cancel_buttons = modal_window.find_elements(
            By.CLASS_NAME,
            'close-modal-button'
        )
        cancel_buttons[0].click()

        self.wait_for(lambda: self.assertFalse(
            modal_window.is_displayed()
        ))

    def test_user_is_prompted_to_verify_their_email_address(self):
        """
        If the user clicks "Skip", they are prompted to verify their
        email address.
        """
        self.browser.get(self.live_server_url + '/login')

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

        modal_window = self.browser.find_element(By.ID, 'prompt-window')
        self.wait_for(lambda: self.assertTrue(
            modal_window.is_displayed()
        ))

        # The user clicks the button labeled 'Skip'.
        cancel_buttons = modal_window.find_elements(
            By.CLASS_NAME,
            'close-modal-button'
        )
        cancel_buttons[1].click()

        heading = modal_window.find_element(By.TAG_NAME, 'h2')

        self.wait_for(lambda: self.assertEqual(
            heading.text,
            'Verify Your Email Address'
        ))

        # The user clicks the 'Skip' button again and the modal
        # window closes.
        cancel_buttons = modal_window.find_elements(
            By.CLASS_NAME,
            'close-modal-button'
        )
        cancel_buttons[1].click()

        self.wait_for(lambda: self.assertFalse(
            modal_window.is_displayed()
        ))
