# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20180423_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='career_field',
            field=models.TextField(max_length=100),
        ),
    ]
