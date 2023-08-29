from django.shortcuts import render

from .models  import  tutorial
#Create your views here.
from .forms import blogform


def  blog(request):
	form = blogform()

	if request.method == 'POST':
		form = blogform(request.POST)
		if form.is_valid():
			form.save()

	Tut = tutorial.objects.all()
	context = {
	'Tut': Tut,
	'form': form
	}
	return  render(request, 'blog.html', context)

def  blog_detail(request,pk):
	Tut = tutorial.objects.get(pk=pk)
	context = {
	'Tut': Tut,
	}
	return  render(request, 'blogdetail.html', context)
