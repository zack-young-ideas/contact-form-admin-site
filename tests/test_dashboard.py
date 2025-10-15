"""
Defines tests run against the admin dashboard page.
"""

from tests import base


class DashboardPageTest(base.BaseTestCase):

    def test_must_be_authenticated_in_to_view(self):
        """
        GET requests return 404 if not authenticated.
        """
        self.browser.get(self.live_server_url + '/dashboard')

        self.assertEqual('404 - Not Found', self.browser.title)
        self.assertIn('Page Not Found', self.browser.page_source)
