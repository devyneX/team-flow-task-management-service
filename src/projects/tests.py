from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Task, Role
from datetime import datetime, timedelta
from django.utils import timezone

class ProjectModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_project(self):
        # Create a project
        project = Project.objects.create(
            project_name='Test Project',
            description='This is a test project',
            created_by=self.user,
            deadline=timezone.now() + timedelta(days=7)  # Use timezone.now() instead of datetime.now()
        )

        # Retrieve the created project from the database
        saved_project = Project.objects.get(project_name='Test Project')

        # Check if the retrieved project matches the created project
        self.assertEqual(saved_project.project_name, 'Test Project')
        self.assertEqual(saved_project.description, 'This is a test project')
        self.assertEqual(saved_project.created_by, self.user)
        self.assertTrue(saved_project.deadline > timezone.now())
        
class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test project
        self.project = Project.objects.create(
            project_name='Test Project',
            description='This is a test project',
            created_by=self.user,
            deadline=timezone.now() + timedelta(days=7)
        )

    def test_create_task(self):
        # Create a task
        task = Task.objects.create(
            task_name='Test Task',
            task_state='todo',
            project=self.project,
            created_by=self.user,
            assigned_to=self.user,
            deadline=timezone.now() + timedelta(days=3),
            details='This is a test task'
        )

        # Retrieve the created task from the database
        saved_task = Task.objects.get(task_name='Test Task')

        # Check if the retrieved task matches the created task
        self.assertEqual(saved_task.task_name, 'Test Task')
        self.assertEqual(saved_task.task_state, 'todo')
        self.assertEqual(saved_task.project, self.project)
        self.assertEqual(saved_task.created_by, self.user)
        self.assertEqual(saved_task.assigned_to, self.user)
        self.assertTrue(saved_task.deadline > timezone.now())
        self.assertEqual(saved_task.details, 'This is a test task')


class RoleModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test project
        self.project = Project.objects.create(
            project_name='Test Project',
            description='This is a test project',
            created_by=self.user,
            deadline=timezone.now() + timedelta(days=7)
        )

    def test_create_role(self):
        # Create a role
        role = Role.objects.create(
            project=self.project,
            user=self.user,
            role='admin'
        )

        # Retrieve the created role from the database
        saved_role = Role.objects.get(user=self.user)

        # Check if the retrieved role matches the created role
        self.assertEqual(saved_role.project, self.project)
        self.assertEqual(saved_role.user, self.user)
        self.assertEqual(saved_role.role, 'admin')

