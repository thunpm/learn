from django.urls import path
from . import views

app_name = 'hrm'

urlpatterns = [
    path('login/', views.login, name="login"),
]