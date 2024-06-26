from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'sport'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.sign_in, name='signin'),
    path('signup', views.sign_up, name='signup'),
    path('signout/', views.sign_out, name='signout'),
    path('user_list', views.user_list, name='user_list'),
    path('user_list/<int:user_id>', views.user_detail, name='user_detail'),

    path('sports/<int:sport_id>', views.sport_detail, name='sport_detail'),

    path('create_contest', views.create_contest, name='create_contest'),
    path('contest/<int:contest_id>', views.contest_detail, name='contest_detail'),
    path('contest/<int:contest_id>/join', views.join_contest, name='join_contest'),
    path('contest/<int:contest_id>/unjoin', views.unjoin, name='unjoin'),
    path('contest/<int:contest_id>/cancel', views.cancel_contest, name='cancel_contest'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
