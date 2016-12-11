from django.conf.urls import url

from . import views

app_name = 'twitter'

urlpatterns = [
    url(r'^user/register/$', views.register_user, name='register_user'),
    url(r'^user/login/$', views.login_user, name='login_user'),
    url(r'^user/logout/$', views.logout_user, name='logout_user'),
    url(r'^user/$', views.profile, name='profile_user'),
    url(r'', views.index, name='index'),
]