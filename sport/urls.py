from django.urls import path

from . import views

app_name = 'sport'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.sign_in, name='signin'),
    path('signup', views.sign_up, name='signup'),
    path('signout/', views.sign_out, name='signout'),
]
