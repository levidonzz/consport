from django.urls import path

from . import views

app_name = 'sport'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('add_user/', views.add_user, name='add_user'),
]
