from django.shortcuts import render
from django.http import HttpResponse
from article.models import article


def hello(request):
	name = "Mike"
	html = "<html><body>Hi %s , this seems to have worked!</body></html>" % name
	return HttpResponse(html)
# Create your views here.

def articles(request):
	return render_to_response('articles.html',
								{'articles': Article.objects.all() })

def article(request, article_id=1):
	return render_to_response('article.html',
								{'article': Article.objects.get(id=article_id) })