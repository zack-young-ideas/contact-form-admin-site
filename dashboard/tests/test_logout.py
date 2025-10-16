from django.contrib.auth import get_user_model
from django.test import Client, TestCase


User = get_user_model()


class LogoutHandlerTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            'admin',
            'admin@example.com',
            '92vLyG-Ly4!q'
        )

    def test_redirects_user_to_login_page(self):
        self.client.force_login(self.user)

        response = self.client.get('/logout')

        self.assertRedirects(response, '/login')

    def test_raises_404_if_user_is_not_authenticated(self):
        response = self.client.get('/logout')

        self.assertEqual(response.status_code, 404)
