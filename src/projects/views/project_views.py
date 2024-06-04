from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.projects.models import Project
from src.projects.serializers.project_serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
