from django.conf.urls import include, url
from . import views


urlpatterns=[
	url(r'^newsletter/$', views.home, name='home'),
	url(r'^contact/$', views.contact, name='contact'),
]