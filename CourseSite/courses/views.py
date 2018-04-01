from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



from django.views import generic

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout

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



class UserFormView(View):
	form_class = UserForm
	template_name = 'courses/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})


	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			#returns User objecyts if credentials are correct

			user = authenticate(username = username, password = password)
			
			if user is not None:

				if user.is_active:
					login(request,user)
					return render(request, 'courses/index.html')

		return render(request, self.template_name, {'form': form})



def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'courses/index.html')

			else:
				return render(request, 'courses/login.html', {'error_message':'Your account has been disabled'})
		
		else:
			return render(request,'courses/login.html',{'error_message':'invalid login'})
	
	return render(request, 'courses/login.html')



def logout_user(request):

	logout(request)
	#form = UserForm(request.POST or None)
	return render(request, 'courses/login.html')




# Create your views here.
