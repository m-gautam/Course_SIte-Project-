# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_remove_course_prereq_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='career_field',
        ),
    ]