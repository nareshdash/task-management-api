from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="demo",
            password="demo@123"
        )

    def test_login_success(self):
        response = self.client.post(
            "/api/login/",
            {
                "username": "demo",
                "password": "demo@123"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_login_failed(self):
        response = self.client.post(
            "/api/login/",
            {
                "username": "demo",
                "password": "wrongpassword"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)