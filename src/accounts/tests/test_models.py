import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):

    def setUp(self):
        self.model = get_user_model()

    def test_create_user(self):
        user = self.model.objects.create_user(uuid.uuid4(), 'test', 'test@test.com')

        self.assertFalse(user.is_superuser, 'is_superuser should be False')
        self.assertFalse(user.is_staff, 'is_staff should be False')
        self.assertFalse(user.has_usable_password(), 'Password should not be set')

        with self.assertRaises(TypeError):
            self.model.objects.create_user()

        with self.assertRaises(ValueError):
            self.model.objects.create_user(uuid.uuid4(), username='', email='test@test.')

        with self.assertRaises(ValueError):
            self.model.objects.create_user(uuid.uuid4(), username='test', email='')

    def test_create_superuser(self):
        user = self.model.objects.create_superuser('test', 'test@test.com', 'password')

        self.assertTrue(user.is_superuser, 'is_superuser should be True')
        self.assertTrue(user.is_staff, 'is_staff should be True')
        self.assertTrue(user.has_usable_password(), 'Password should be set')

        with self.assertRaises(ValueError):
            self.model.objects.create_superuser('test', 'test@test.com', 'password', is_superuser=False)

        with self.assertRaises(ValueError):
            self.model.objects.create_superuser('test', 'test@tes.com', 'password', is_staff=False)
