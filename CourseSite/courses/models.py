# -*- coding: utf-8		 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import CharField, Model
import ast
#from custom.fields import SeparatedValuesField 	

from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
	course_code = models.CharField(max_length = 10)
	course_name = models.CharField(max_length = 100)
	course_credits = models.IntegerField(default =0)
	prereq_courses = ArrayField(models.CharField(max_length=200, default = 'NULL'), blank=True)
	career_field = models.CharField(max_length = 100)	
	
	def __str__(self):
		return self.course_code



class Reviews(models.Model):

	class Meta:
		verbose_name_plural = 'Reviews'

	ccode = models.CharField(max_length = 10, default = 'NULL')
	professor = models.CharField(max_length = 100, default = 'NULL')
	semester = models.CharField(max_length = 10, default = 'NULL')
	offered_year = models.IntegerField(default =0)
	review = models.CharField(max_length = 3000 , default = 'NULL')

	def __str__(self):
		return self.ccode







# Create your models here.
