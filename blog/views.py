from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author' : 'Domo X',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 22, 2020'
    },
    {
        'author' : 'Ray X',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 23, 2020'
    },
    {
        'author' : 'Saegar X',
        'title' : 'Blog Post 3',
        'content' : 'Third post content',
        'date_posted' : 'April 24, 2020'
    },{
        'author' : 'Joe X',
        'title' : 'Blog Post 4',
        'content' : 'Fourth post content',
        'date_posted' : 'April 25, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
