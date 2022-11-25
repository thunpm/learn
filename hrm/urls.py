from django.urls import path
from . import views

app_name = 'hrm'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('user/', views.UserListView.as_view(), name="list_user"),
    path('user/create', views.UserCreateView.as_view(), name="create_user"),
    path('user/<str:pk>/', views.UserUpdateView.as_view(), name="update_user"),
    path('user/delete/<str:pk>/', views.UserDeleteView.as_view(), name="delete_user"),
]