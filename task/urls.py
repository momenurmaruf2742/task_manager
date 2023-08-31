from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    # ... Other URLs

    # User Registration
    path('register/', views.register, name='register'),

    # User Login
    path('login/', views.user_login, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    # Create Task
    path('create/', views.create_task, name='task-create'),
    path('', views.task_list, name='task-list'),
    path('detail/<int:task_id>/', views.task_detail, name='task-detail'),
    # Edit Task
    path('edit/<int:task_id>/', views.edit_task, name='task-edit'),

    # Delete Task
    path('delete/<int:task_id>/', views.delete_task, name='task-delete'),

    # User Logout
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('404/', views.error_404, name='error-404'),
]
