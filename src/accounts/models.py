from rest_framework_simplejwt.models import TokenUser


class User(TokenUser):

    @property
    def name(self) -> str:
        return self.token.get('first_name', '') + ' ' + self.token.get('last_name', '')

    @property
    def email(self) -> str:
        return self.token.get('email', '')

    def __str__(self) -> str:
        return self.username
