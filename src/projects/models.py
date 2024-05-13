from django.db import models

from src.core.models import BaseModel, AuditModelMixin


class Project(BaseModel, AuditModelMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # created by inherited from AuditModelMixin does not work as owner as ownership can be transferred
    owner = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='projects', related_query_name='project'
    )
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.owner}'
