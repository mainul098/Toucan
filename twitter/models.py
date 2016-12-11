from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=265)
    user = models.ForeignKey(User, verbose_name='created by')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} : {1}'.format(self.user.username, self.content[:20])


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='users')
    follower = models.ForeignKey(User, related_name='followers')  #whom the user following, bit confusing
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} followed {1}'.format(self.user.username,self.follower.username)

    class Meta:
        unique_together = ('user', 'follower')


def get_follower_tweets(user):
    return Tweet.objects.filter(user__followers__user=user).order_by('modified_date')[:10]


def add_follower(user, follower):
    relationship = Follow.objects.create(user, follower)
    relationship.save()


def remove_follower(user, follower):
    relationship = Follow.objects.filter(user=user, follower=follower)
    relationship.delete()
