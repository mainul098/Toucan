# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20161210_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='created_by',
            new_name='user',
        ),
    ]
