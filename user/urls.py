from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('users/', views.users, name='users'),
    path('register/', views.add_user, name='register'),
]
