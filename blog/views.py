from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    about_title = {'title': 'About'}
    return render(request, 'blog/about.html', about_title)
