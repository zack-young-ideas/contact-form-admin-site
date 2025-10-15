from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from login import forms


User = get_user_model()


class LoginPageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            'admin',
            'admin@example.com',
            '92vLyG-Ly4!q'
        )

    def test_uses_login_page_template(self):
        response = self.client.get('/login')

        self.assertTemplateUsed(response, 'login/login_page.html')

    def test_login_page_uses_login_form(self):
        response = self.client.get('/login')

        self.assertIsInstance(response.context['form'], forms.LoginForm)

    def test_redirects_to_dashboard(self):
        response = self.client.post(
            '/login',
            data={
                'username': 'admin',
                'password': '92vLyG-Ly4!q',
            }
        )

        self.assertRedirects(response, '/dashboard')

    def test_displays_error_message_given_invalid_username(self):
        response = self.client.post(
            '/login',
            data={
                'username': 'invalidUsername',
                'password': '92vLyG-Ly4!q',
            }
        )

        self.assertContains(
            response,
            '<p id="error-message">Invalid username or password</p>'
        )

    def test_displays_error_message_given_invalid_password(self):
        response = self.client.post(
            '/login',
            data={
                'username': 'admin',
                'password': 'invalidPassword',
            }
        )

        self.assertContains(
            response,
            '<p id="error-message">Invalid username or password</p>'
        )


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

        self.assertTemplateUsed(response, 'dashboard.html')
