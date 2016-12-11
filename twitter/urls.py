from django.conf.urls import url

from . import views

app_name = 'twitter'

urlpatterns = [
    url(r'^user/register/$', views.register_user, name='register_user'),
    url(r'^user/login/$', views.login_user, name='login_user'),
    url(r'^user/logout/$', views.logout_user, name='logout_user'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.profile, name='profile_user'),
    url(r'^tweet/$', views.create_tweet, name='create_tweet'),
    url(r'^follow/(?P<user_id>[0-9]+)/$', views.add_follow, name='follow'),
    url(r'^unfollow/(?P<user_id>[0-9]+)/$', views.remove_follow, name='unfollow'),
    url(r'', views.index, name='index'),
]