from unittest import TestCase

import requests.exceptions
from rest_framework.exceptions import ValidationError

from src.projects.utils import get_user_detail_from_id, get_user_detail_from_ids


class TestUserAPIUtils(TestCase):

    def test_get_user_by_ids_with_valid_data(self):
        uuids = [
            '4a6402d2-4c7c-424f-b70c-a0159047140c', 'f6b7c0e2-b86a-4fde-8e9b-dbfb05dc1289',
            '7ae54971-d25f-472a-b116-4696a456d4e9', '39d00d94-b4f3-42e0-a265-957f31edda8e',
            'cfac4916-f674-424a-969b-ce204493691c', '550e8400-e29b-41d4-a716-446655440000'
        ]

        expected_response = {
            '4a6402d2-4c7c-424f-b70c-a0159047140c': {
                'uuid': '4a6402d2-4c7c-424f-b70c-a0159047140c',
                'username': 'test1',
                'email': 'test1@test.com',
                'first_name': '',
                'last_name': '',
                'is_staff': False,
                'is_superuser': False
            },
            'f6b7c0e2-b86a-4fde-8e9b-dbfb05dc1289': {
                'uuid': 'f6b7c0e2-b86a-4fde-8e9b-dbfb05dc1289',
                'username': 'test2',
                'email': 'test2@test.com',
                'first_name': '',
                'last_name': '',
                'is_staff': False,
                'is_superuser': False
            },
            '7ae54971-d25f-472a-b116-4696a456d4e9': {
                'uuid': '7ae54971-d25f-472a-b116-4696a456d4e9',
                'username': 'test3',
                'email': 'test3@test.com',
                'first_name': '',
                'last_name': '',
                'is_staff': False,
                'is_superuser': False
            },
            '39d00d94-b4f3-42e0-a265-957f31edda8e': {
                'uuid': '39d00d94-b4f3-42e0-a265-957f31edda8e',
                'username': 'test4',
                'email': 'test4@test.com',
                'first_name': '',
                'last_name': '',
                'is_staff': False,
                'is_superuser': False
            },
            'cfac4916-f674-424a-969b-ce204493691c': {
                'uuid': 'cfac4916-f674-424a-969b-ce204493691c',
                'username': 'test5',
                'email': 'test5@test.com',
                'first_name': '',
                'last_name': '',
                'is_staff': False,
                'is_superuser': False
            },
            '550e8400-e29b-41d4-a716-446655440000': 'User not found'
        }

        user_info = get_user_detail_from_ids(uuids)

        for uuid, user_detail in user_info.items():
            try:
                # if the user is not found, the user_detail will be a string
                self.assertDictEqual(user_detail, expected_response[uuid])
            except AssertionError:
                try:
                    self.assertEqual(user_detail, expected_response[uuid])
                except AssertionError as e:
                    raise e

    def test_get_user_by_ids_with_invalid_data(self):
        uuids = [
            'invalid_uuid',
        ]

        with self.assertRaises(ValidationError):
            get_user_detail_from_ids(uuids)

    def test_get_user_detail_from_id(self):
        uuid = '4a6402d2-4c7c-424f-b70c-a0159047140c'

        expected_response = {
            'uuid': '4a6402d2-4c7c-424f-b70c-a0159047140c',
            'username': 'test1',
            'email': 'test1@test.com',
            'first_name': '',
            'last_name': '',
            'is_staff': False,
            'is_superuser': False
        }

        user_detail = get_user_detail_from_id(uuid)

        self.assertDictEqual(user_detail, expected_response)

    def test_get_user_detail_from_id_with_wrong_uuid(self):
        uuid = '550e8400-e29b-41d4-a716-446655440000'

        with self.assertRaises(requests.exceptions.RequestException):
            get_user_detail_from_id(uuid)
