from django.urls import path
from .views import Tasklist, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
     # Login
    path('', CustomLoginView.as_view(), name='login'),
    # Logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Signup
    path('register/', RegisterPage.as_view(), name='register'),
    # Home
    path('tasks/', Tasklist.as_view(), name='tasks'),
    # Task Detail
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    # Task Create  
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    # Task Update
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # Task Delete
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]