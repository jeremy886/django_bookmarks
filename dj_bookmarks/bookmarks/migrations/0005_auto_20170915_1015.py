# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 17:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0004_collection'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('user', 'slug')]),
        ),
    ]
