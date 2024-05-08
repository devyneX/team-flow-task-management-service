from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# from src.projects.models import Project, Role, Task


class ProjectListViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = APIClient()
        self.url = reverse('project-list')

    def test_get_project_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        data = {
            'project_name': 'Test Project',
            'description': 'This is a test project',
            'created_by': self.user
        }
        response = self.client.post(self.url, data)
        print(response.status_code)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class ProjectDetailViewTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.project = Project.objects.create(project_name='Test Project', description='This is a test project')
#         self.client = APIClient()
#         self.url = reverse('project-detail', args=[self.project.pk])

#     def test_get_project_detail(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_project(self):
#         data = {'project_name': 'Updated Project Name',
#         'description': 'Updated description', 'created_by': self.user}
#         response = self.client.put(self.url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['project_name'], 'Updated Project Name')
#         self.assertEqual(response.data['description'], 'Updated description')

#     def test_delete_project(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

# # Similarly, you can write tests for TaskListView, TaskDetailView, RoleListView, and RoleDetailView
