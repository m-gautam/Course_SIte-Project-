# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_reviews_ccode'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='ccode',
            field=models.CharField(default='NULL', max_length=10),
        ),
    ]
