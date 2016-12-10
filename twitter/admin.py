from django.contrib import admin

from twitter.models import Follow, Tweet

admin.site.register(Tweet)
admin.site.register(Follow)
