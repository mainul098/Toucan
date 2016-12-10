from django.contrib.auth.models import User
from django.db import models


class Twit(models.Model):
    content = models.CharField(max_length=265)
    created_by = models.ForeignKey(User, verbose_name='created by')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='user')
    follower = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

