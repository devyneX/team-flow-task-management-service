from django.test import SimpleTestCase
from django.urls import resolve, reverse

from src.projects.views import (
    ProjectDetailView, ProjectListView, RoleDetailView, RoleListView,
    TaskDetailView, TaskListView
)


class TestUrls(SimpleTestCase):

    def test_project_list_url_resolves(self):
        url = reverse('project-list')
        self.assertEqual(resolve(url).func.view_class, ProjectListView)

    def test_project_detail_url_resolves(self):
        url = reverse(
            'project-detail', args=['00000000-0000-0000-0000-000000000000']
        )
        self.assertEqual(resolve(url).func.view_class, ProjectDetailView)

    def test_task_list_url_resolves(self):
        url = reverse('task-list')
        self.assertEqual(resolve(url).func.view_class, TaskListView)

    def test_task_detail_url_resolves(self):
        url = reverse(
            'task-detail', args=['00000000-0000-0000-0000-000000000000']
        )
        self.assertEqual(resolve(url).func.view_class, TaskDetailView)

    def test_role_list_url_resolves(self):
        url = reverse('roles-list')
        self.assertEqual(resolve(url).func.view_class, RoleListView)

    def test_role_detail_url_resolves(self):
        url = reverse(
            'roles-detail', args=[1]
        )  # You need to pass an integer as argument, as specified in your URL pattern
        self.assertEqual(resolve(url).func.view_class, RoleDetailView)
