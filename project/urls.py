from django.conf.urls import patterns, include, url
from . import views
 
urlpatterns = [
	# url(r'^newsletter/$', views.home, name='home'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
]