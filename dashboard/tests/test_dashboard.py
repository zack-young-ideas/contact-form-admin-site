from django.contrib.auth import get_user_model
from django.test import Client, TestCase


User = get_user_model()


class DashboardTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            'admin',
            'admin@example.com',
            '92vLyG-Ly4!q'
        )

    def test_returns_404_if_not_authenticated(self):
        response = self.client.get('/dashboard')

        self.assertEqual(response.status_code, 404)

    def test_uses_dashboard_template(self):
        self.client.force_login(self.user)

        response = self.client.get('/dashboard')

        self.assertTemplateUsed(response, 'dashboard/dashboard.html')
