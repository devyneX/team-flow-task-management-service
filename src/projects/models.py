# import uuid

from django.contrib.auth.models import User
from django.db import models
from src.core.models import BaseModel


class Project(BaseModel):
    # uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False
    # )
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.project_name


class Task(BaseModel):
    # uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False
    # )
    task_name = models.CharField(max_length=100)
    STATE_CHOICES = (('todo', 'To Do'), ('in_progress', 'In Progress'),
                     ('done', 'Done'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_state = models.CharField(max_length=20, choices=STATE_CHOICES)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_tasks'
    )
    deadline = models.DateTimeField(
        null=True, blank=True
    )  # Optional deadline for the task
    details = models.TextField(null=True, blank=True)  # Details of the task

    def __str__(self):
        return f'{self.project.project_name} - {self.task_name}'


class Role(BaseModel):
    ROLES_CHOICES = (('admin', 'Admin'), ('moderator', 'Moderator'),
                     ('user', 'User'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} in {self.project.project_name} as {self.role}'
