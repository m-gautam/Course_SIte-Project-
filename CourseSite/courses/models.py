# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	course_code = models.CharField(max_length = 10)
	course_name = models.CharField(max_length = 100)
	course_credits = models.IntegerField(default =0)
	prereq_courses = models.CharField(max_length = 1000 )
	career_field = models.CharField(max_length = 100, default = 'NULL')

	def __str__(self):
		return self.course_code


class Reviews(models.Model):
	ccode = models.CharField(max_length = 10, default = 'NULL')
	professor = models.CharField(max_length = 100, default = 'NULL')
	semester = models.CharField(max_length = 10, default = 'NULL')
	offered_year = models.IntegerField(default =0)
	review = models.CharField(max_length = 3000 , default = 'NULL')

	def __str__(self):
		return self.ccode


# Create your models here.
