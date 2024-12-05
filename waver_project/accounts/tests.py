from django.test import TestCase
from django.urls import reverse

class UserLoginTest(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)  # Перевірка, чи доступна сторінка