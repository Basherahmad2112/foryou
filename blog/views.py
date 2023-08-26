from django.shortcuts import render

from .models  import  tutorial
#Create your views here.

def  blog(request):
	Tut = tutorial.objects.all()
	context = {
	'Tut': Tut,
	}
	return  render(request, 'blog.html', context)

def  blog_detail(request,pk):
	Tut = tutorial.objects.get(pk=pk)
	context = {
	'Tut': Tut,
	}
	return  render(request, 'blogdetail.html', context)
