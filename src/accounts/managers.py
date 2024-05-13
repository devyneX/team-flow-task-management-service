import uuid

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, uuid_val, username, email, **extra_fields):
        if not uuid_val:
            raise ValueError('The UUID must be set')

        if not username:
            raise ValueError('The Username must be set')
        username = self.model.normalize_username(username)

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)

        user = self.model(uuid=uuid_val, username=username, email=email, **extra_fields)

        # TODO: gotta change this later
        if extra_fields.get('is_staff', False) is False:
            user.set_unusable_password()
            user.save()
            return user

        if extra_fields.get('password', None) is None:
            raise ValueError('The Password must be set for staffs')

        user.set_password(extra_fields.pop('password'))
        user.save()
        return user

    # TODO: gotta change this later
    # superuser should not be created here
    # should copy the superuser from the auth service
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields['password'] = password

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('password', None)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        uuid_val = uuid.uuid4()

        return self.create_user(uuid_val, username, email, **extra_fields)
