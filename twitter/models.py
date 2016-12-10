from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=265)
    created_by = models.ForeignKey(User, verbose_name='created by')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='users')
    follower = models.ForeignKey(User, related_name='followers')
    created_date = models.DateTimeField(auto_now_add=True)

