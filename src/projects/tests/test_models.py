import uuid
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from src.accounts.models import User
from src.projects.models import Project


class ProjectModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(uuid_val=uuid.uuid4(), username='test', email='test@test.com')

    def test_create_project(self):
        project = Project.objects.create(
            created_by=self.user,
            updated_by=self.user,
            name='Test Project',
            description='Test Description',
            deadline=timezone.now() + timedelta(days=7)
        )

        self.assertIs(project.owner, self.user)
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.description, 'Test Description')
        self.assertEqual(project.deadline, project.deadline)
