import os  # noqa
from pathlib import Path

from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

include('base.py')
include('rest_framework.py')
include('auth_service.py')
