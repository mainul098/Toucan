from django.contrib import admin

from twitter.models import Twit, UserProfile

admin.site.register(Twit)
admin.site.register(UserProfile)
