from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sports/<int:sport_id>/', views.sport, name='sports'),
    path('contests/<int:contest_id>', views.contest, name='contest'),
]