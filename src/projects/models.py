from django.db import models

from src.core.models import AuditModelMixin, BaseModel
from src.projects.managers.member_manager import MemberManager
from src.projects.managers.project_manager import ProjectManager


class Project(BaseModel, AuditModelMixin):  # type: ignore
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # created by inherited from AuditModelMixin does not work as owner as ownership can be transferred
    owner = models.UUIDField()
    deadline = models.DateTimeField(null=True, blank=True)

    objects = ProjectManager()

    def __str__(self):
        return f'{self.name} - {self.owner}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.owner = self.created_by
        super().save(*args, **kwargs)


class Member(BaseModel, AuditModelMixin):  # type: ignore
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members', related_query_name='member')
    user = models.UUIDField()

    objects = MemberManager()

    @property
    def removed(self):
        return self.deleted

    @property
    def added_by(self):
        return self.created_by

    @added_by.setter
    def added_by(self, adder):
        if self.added_by:
            print(f'added_by: {self.added_by}')
            raise ValueError('added_by cannot be changed once it is set')
        self.created_by = adder

    @property
    def removed_by(self):
        return self.updated_by if self.removed else None

    @removed_by.setter
    def removed_by(self, remover):
        if self.removed_by:
            raise ValueError('removed_by cannot be changed once it is set')
        self.updated_by = remover
