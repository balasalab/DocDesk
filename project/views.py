from django.shortcuts import render

# Create your views here.
from project.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .authenticate import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
# from .backends import EmailAuthBackend


def login(request):
	"""
	Log in view
	"""
	LoginForm = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			if user is not None:
				if user.is_active:
					django_login(request, user)
					return redirect('/home')
		else:
			return render(request, 'project/login.html', {'form': LoginForm})

	else:
		if request.user.is_authenticated():
			return redirect('/home')
			
		content = {
		'form': LoginForm
		}
		return render(request, 'project/login.html', content)

def login_old(request):
	"""
	Log in view
	"""
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			print (user)
			if user is not None:
				if user.is_active:
					django_login(request, user)
					return redirect('/home')
	else:
		if request.user.is_authenticated():
			return redirect('/home')
			
		form = AuthenticationForm()
		content = {
		'form': form
		}
		return render(request, 'project/login.html', content)

	# if user is not None:
	# 	return render(request, 'project/home.html', {'user':user})
	# else:
	# 	return render(request, 'project/login.html', {})
	return render_to_response('project/home.html', {
		'form': form,
	}, context_instance=RequestContext(request))

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'project/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'project/success.html',
    )
 
# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
def logout_page(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/')

def login_page(request):
    return render_to_response(
    'project/login.html',
    )
 
@login_required
def home(request):
    return render_to_response(
    'project/home.html',
    { 'user': request.user }
    )