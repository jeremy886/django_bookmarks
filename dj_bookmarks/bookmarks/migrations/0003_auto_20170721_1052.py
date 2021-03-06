# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20170714_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
