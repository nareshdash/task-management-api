from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class PermissionTestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(
            username="user1",
            password="pass123"
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="pass123"
        )

        # Login user1
        response = self.client.post(
            "/api/login/",
            {
                "username": "user1",
                "password": "pass123"
            }
        )

        self.token = response.data["access"]
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_user_cannot_access_other_user_task(self):
        # Create task with user1
        task = self.client.post(
            "/api/tasks/",
            {
                "title": "User1 Task",
                "description": "Test"
            }
        )

        task_id = task.data["id"]

        # Login as user2
        response = self.client.post(
            "/api/login/",
            {
                "username": "user2",
                "password": "pass123"
            }
        )

        token2 = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token2}"
        )

        # Try accessing user1 task
        response = self.client.get(f"/api/tasks/{task_id}/")

        self.assertIn(
            response.status_code,
            [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND]
        )