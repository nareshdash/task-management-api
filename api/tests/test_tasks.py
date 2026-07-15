from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="demo",
            password="demo@123"
        )

        # Login user
        response = self.client.post(
            "/api/login/",
            {
                "username": "demo",
                "password": "demo@123"
            }
        )

        self.token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_create_task(self):
        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Test Task",
                "description": "Test Description"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Task")

    def test_get_tasks(self):
        # Create task first
        self.client.post(
            "/api/tasks/",
            {
                "title": "Task 1",
                "description": "Desc"
            }
        )

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_task(self):
        task = self.client.post(
            "/api/tasks/",
            {
                "title": "Old Title",
                "description": "Desc"
            }
        )

        task_id = task.data["id"]

        response = self.client.put(
            f"/api/tasks/{task_id}/",
            {
                "title": "Updated Title",
                "description": "Updated Desc"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_task(self):
        task = self.client.post(
            "/api/tasks/",
            {
                "title": "Delete Task",
                "description": "Desc"
            }
        )

        task_id = task.data["id"]

        response = self.client.delete(f"/api/tasks/{task_id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)