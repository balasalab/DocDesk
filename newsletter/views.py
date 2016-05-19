from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .forms import ContactForm, SignUpForm

def home(request):
	title = "Welcome"
	# if request.user.is_authenticated():
	# 	title = "Doc Desk %s" %(request.user)
	
	# add a form
	form = SignUpForm(request.POST or None)

	context = {
		"title":title,
		"form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False) #skip saving

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Hey!"

		print (full_name)
		instance.full_name = full_name
		instance.save()

		context = {
			"title":"Thank you",
		}

	return render(request, 'newsletter/home.html', context)
	# return render(request, 'base.html', context)

def contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		# for key, value in form.cleaned_data.items():
		# 	print (key, value)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_name = form.cleaned_data.get("name")

		subject = "DocDesk contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
		contact_message = "%s: %s via %s"%(
			form_name, 
			form_message, 
			form_email)
		some_html_message = """
		<h3>Welcome DocDesk</h3>
		"""
		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message=some_html_message,
				fail_silently=False
				)

		# print (email, message, name)

	context = {
		"form" : form,
	}
	return render(request, 'newsletter/contact_from.html', context)