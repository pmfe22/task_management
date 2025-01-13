from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView
from .views import DeleteTaskView
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # برای APIهای RESTful
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/create/', views.CreateTaskView.as_view(), name='create_task'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),  # جزئیات وظیفه
    path('tasks/edit/<int:pk>/', views.EditTaskView.as_view(), name='edit_task'),
    path('tasks/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
]
