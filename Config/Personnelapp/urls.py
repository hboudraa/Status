from django.urls import path
from . import views

app_name = 'personnel'

urlpatterns = [
    path('users/', views.users, name='users'),
]