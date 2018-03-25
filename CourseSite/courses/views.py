from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course, Reviews


def index(request):
	all_courses = Course.objects.all()
	all_reviews = Reviews.objects.all()
	template = loader.get_template('courses/index.html')
	context = {
		'all_courses' : all_courses,
	}
	return HttpResponse(template.render(context, request))

def detail(request):
	search_str = request.POST['q']
	p = Course.objects.filter(course_code = search_str)
	q = Reviews.objects.filter(ccode = search_str)
	return render(request, 'courses/detail.html',{'p':p, 'q':q} )

def add_course(request):
	if request.method == 'GET' :
		template = loader.get_template('courses/acourses.html')
		context = {
		}
		return HttpResponse(template.render(context, request))
	else :
		course_code= request.POST['course_code']
		course_name= request.POST['course_name']
		course_credits = request.POST['course_credits']
		prereq_courses = request.POST['pcourses']
		course = Course(
			course_code=course_code,
			course_name=course_name,
			course_credits= course_credits,
			prereq_courses=''
			)
		course.save()
		p=Course.objects.all();
		return render(request, 'courses/detail.html', {'p':p})

def add_reviews(request):
		if request.method == 'GET' :
			template = loader.get_template('courses/areviews.html')
			context = {
			}
			return HttpResponse(template.render(context, request))
		else:
			ccode = request.POST['ccode']
			professor = request.POST['professor']
			offered_year = request.POST['offered_year']
			semester = request.POST['semester']
			review = request.POST['review']

			review = Reviews(
				ccode = ccode,
				professor = professor,
				offered_year = offered_year,
				semester = semester,
				review = review,
			)
			review.save()
			allreviews = Reviews.objects.all();
			return render(request, 'courses/index.html', {'allreviews' : allreviews})

def cfield(request):
	search_str = request.POST['p']
	field = Course.objects.filter( career_field = search_str);
	return render (request, 'courses/careerfields.html', {'field' : field})

def profdetails(request):
	search_str = request.POST['p']
	field = Reviews.objects.filter(professor = search_str)
	return render (request, 'courses/profdetails.html', {'field': field})



# Create your views here.
