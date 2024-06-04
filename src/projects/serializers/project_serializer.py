from rest_framework import serializers

from src.accounts.serializers.user_serializer import UserSerializer
from src.projects.models import Member, Project


class MemberSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(allow_null=True)

    class Meta:
        model = Member
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializerWithMemberList(ProjectSerializer):
    members = serializers.ListSerializer(child=MemberSerializer)
