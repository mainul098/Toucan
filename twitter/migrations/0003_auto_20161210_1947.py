# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 19:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0002_auto_20161210_1855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'follower')]),
        ),
    ]
