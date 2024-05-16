from rest_framework import serializers

from src.accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
        )

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
