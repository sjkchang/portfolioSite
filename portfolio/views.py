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
    return render(request, 'portfolio/portfolio-temp-base.html', context)


def resume(request):
    context = {
        'title': 'Resume'
    }
    return render(request, 'portfolio/portfolio-resume.html', context)


def projects(request):
    context = {
        'title': 'Projects'
    }
    return render(request, 'portfolio/portfolio-projects.html', context)


def contact(request):
    context = {
        'title': 'Contact Me'
    }
    return render(request, 'portfolio/portfolio-contact.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'portfolio/portfolio-about.html', context)
