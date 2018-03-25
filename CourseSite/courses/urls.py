from django.conf.urls import url
from . import views 

urlpatterns = [
	  url(r'^$', views.index, name = 'index'),
	  url(r'^detail/', views.detail, name = 'detail'),
	  url(r'^add_course/', views.add_course, name = 'add_course'),
	  url(r'^add_review/', views.add_reviews, name = 'add_reviews'),
	  url(r'^cfield/', views.cfield, name = 'cfield'),	
	  url(r'^profdetails/', views.profdetails, name ='profdetails')

	  #url(r'^timeslots/', views.timeslots, name = 'timeslots')
]
