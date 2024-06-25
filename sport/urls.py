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
    path('<int:sport_id>', views.sport_detail, name='sport_detail'),
    path('create_contest', views.create_contest, name='create_contest'),
    path('user_list', views.user_list, name='user_list'),
    path('user_list/<int:user_id>', views.user_detail, name='user_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
