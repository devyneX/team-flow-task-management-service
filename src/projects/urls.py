from django.urls import path
from .views import ProjectListView, ProjectDetailView, TaskListView, TaskDetailView, RoleListView, RoleDetailView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<uuid:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('roles/', RoleListView.as_view(), name='roles-list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='roles-detail'),
]
