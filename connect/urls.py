from django.urls import path

from . import views

app_name = 'connect'
urlpatterns = [
    path('', views.index, name='index'),
    path('sports/<int:sport_id>/', views.sport, name='sport'),
    path('contests/<int:contest_id>', views.contest, name='contest'),
    path('users/', views.all_user, name='users'),
    path('join_contest/', views.join_contest, name='join_contest'),
    path('create_contest/', views.sport, name='create_contest'),
]