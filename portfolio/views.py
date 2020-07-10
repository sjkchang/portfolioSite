from django.http import Http404 , HttpResponse
from django.shortcuts import render

posts = [
    {
        'name': 'Steven',
        'age': 20
    }
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'portfolio/portfolio-base.html', context)


def resume(request):
    context = {
        'title': 'Resume'
    }
    return render(request, 'portfolio/portfolio-resume.html', context)
