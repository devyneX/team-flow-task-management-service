import json

import requests
from django.conf import settings

from src.accounts.serializers.user_serializer import ListUserUUIDSerializer


def get_user_detail_from_ids(uuids):
    """
    Get user details from a list of user UUIDs.
    """
    serializer = ListUserUUIDSerializer(data=uuids)
    serializer.is_valid(raise_exception=True)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    req_data = json.dumps(serializer.data)

    try:
        response = requests.post(f'{settings.AUTH_SERVICE_USERS_BY_IDS_URL}', data=req_data, headers=headers)
    except requests.exceptions.RequestException as e:
        raise e

    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.RequestException(
            f'Request failed with status code {response.status_code}.'
            f' Details: {response.text}'
        )


def get_user_detail_from_id(uuid):
    """
    Get user details from a user UUID.
    """
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    try:
        response = requests.get(f'{settings.AUTH_SERVICE_USER_URL}/{uuid}', headers=headers)
    except requests.exceptions.RequestException as e:
        raise e

    if response.status_code == 200:
        return response.json()
    else:
        raise requests.exceptions.RequestException(
            f'Request failed with status code {response.status_code}.'
            f' Details: {response.text}'
        )
