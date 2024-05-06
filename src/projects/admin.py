from django.contrib import admin

from .models import Project, Role, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Role)
