from rest_framework_simplejwt.models import TokenUser


class User(TokenUser):
    @property
    def name(self) -> str:
        return self.token.get("name", "")

    @property
    def email(self) -> str:
        return self.token.get("email", "")
