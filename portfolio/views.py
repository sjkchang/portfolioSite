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
    return render(request, 'portfolio/portfolio-home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'portfolio/portfolio-about.html', context)
