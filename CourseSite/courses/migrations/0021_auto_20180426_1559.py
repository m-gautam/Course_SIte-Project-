# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20180426_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='career_field',
        ),
        migrations.AddField(
            model_name='course',
            name='career_field',
            field=models.TextField(default='NULL', verbose_name='self'),
        ),
    ]
