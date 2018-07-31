from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
	arts = models.Article.objects.all()
	return render(request,'blog/index.html',{'arts':arts})

def hpage(request, art_id):
	art = models.Article.objects.get(pk = art_id)
	return render(request,'blog/page.html',{'art':art})

def action(request,art_id):
	if int(art_id) :
		art = models.Article.objects.get(pk = art_id)
		return render(request,'blog/action.html',{'art':art})
	else:
		return render(request,'blog/action.html')
	

def act(request):
	art_id = request.POST.get('art_id')
	if int(art_id):
		title = request.POST.get('title')
		content = request.POST.get('content')
		art = models.Article.objects.get(pk = art_id)
		art.title = title
		art.content = content
		art.save()
		arts = models.Article.objects.all()
		return render(request,'blog/index.html',{'arts':arts})

	title = request.POST.get('title')
	content = request.POST.get('content')
	models.Article.objects.create(title = title, content = content)
	arts = models.Article.objects.all()
	return render(request,'blog/index.html',{'arts':arts})
