from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	name = "Mike"
	html = "<html><body>Hi %s , this seems to have worked!</body></html>" % name
	return HttpResponse(html)
# Create your views here.
