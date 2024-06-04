from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()


class ListUserUUIDSerializer(serializers.Serializer):
    uuids = serializers.ListField(
        child=serializers.UUIDField(),
        allow_empty=False,
    )

    def validate_uuids(self, value):
        result = {}
        for user_uuid in value:
            user_uuid_str = str(user_uuid)
            result[user_uuid_str] = 'User not found'
        return result

    def to_internal_value(self, data):
        return super().to_internal_value({'uuids': data})
