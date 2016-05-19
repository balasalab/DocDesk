from django.conf import settings
from django.shortcuts import render

# Create your views here.

def home(request):
	title = "DocDesk"
	context = {
		"title":title,
	}

	return render(request, 'landing/base.html', context)