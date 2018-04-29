from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



from django.views import generic

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import logout

from django.core.mail import send_mail

from .models import Course, Reviews




from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage








def index(request):
	all_courses = Course.objects.all()
	all_reviews = Reviews.objects.all()
	template = loader.get_template('courses/index.html')
	context = {
		'all_courses' : all_courses,
	}
	return HttpResponse(template.render(context, request))






def detail(request):
	if request.method == 'GET' :
		search_str = request.GET.get('q')
		p = Course.objects.filter(course_code = q)
		q = Reviews.objects.filter(ccode = search_str)
		return render(request, 'courses/detail.html',{'p':p, 'q':q} )
	else:
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
		return render(request, 'courses/index.html', {'p':p})





def add_reviews(request):
		if request.method == 'GET' :
			template = loader.get_template('courses/areviews.html')
			context = {
			}
			return HttpResponse(template.render(context, request))
		else:
			ccode = request.POST['ccode']
			#if ccode == Course.objects.filter(course_code = ccode):
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

			# else:
			# 	return HttpResponse('Course is invalid!')				





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
















def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('courses/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'courses/signup.html', {'form': form})





def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


















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
