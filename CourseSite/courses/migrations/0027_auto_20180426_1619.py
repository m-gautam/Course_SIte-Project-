# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_remove_course_career_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='career_field',
            field=models.TextField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='prereq_courses',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
