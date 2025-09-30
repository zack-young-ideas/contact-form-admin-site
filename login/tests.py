from django.contrib.auth import get_user_model
from django.test import TestCase

from login import forms


User = get_user_model()


class LoginPageTest(TestCase):

    def test_uses_login_page_template(self):
        response = self.client.get('/login')

        self.assertTemplateUsed(response, 'login/login_page.html')

    def test_login_page_uses_login_form(self):
        response = self.client.get('/login')

        self.assertIsInstance(response.context['form'], forms.LoginForm)

    def test_redirects_to_dashboard(self):
        User.objects.create_superuser(
            'admin',
            'admin@example.com',
            '92vLyG-Ly4!q'
        )

        response = self.client.post(
            '/login',
            data={
                'username': 'admin',
                'password': '92vLyG-Ly4!q',
            }
        )

        self.assertRedirects(response, '/dashboard')


class DashboardTest(TestCase):

    def test_uses_dashboard_template(self):
        response = self.client.get('/dashboard')

        self.assertTemplateUsed(response, 'dashboard.html')
