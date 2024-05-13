from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.models import TokenUser

from src.accounts.managers import UserManager


class CustomizedTokenUser(TokenUser):
    @property
    def name(self) -> str:
        return self.token.get("name", "")

    @property
    def email(self) -> str:
        return self.token.get("email", "")

    @property
    def model_user(self):
        return User.objects.get(uuid=self.id)


class User(AbstractUser):
    uuid = models.UUIDField(unique=True, editable=False)
    email = models.EmailField(unique=True)
    objects = UserManager()



