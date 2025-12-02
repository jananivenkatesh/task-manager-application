from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskCompleteToggle

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('toggle-complete/<int:pk>/', TaskCompleteToggle.as_view(), name='task-toggle'),
]
