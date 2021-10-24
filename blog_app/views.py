from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def index(request):
    data = Post.objects.order_by('-id')
    return render(request, 'blog_app/home.html', {"posts" : data})


def single_post(request, id):
    data = Post.objects.get(id=id)
    return render(request, 'blog_app/single_post.html', {"post" : data})

def search(request):
    query = request.GET['q']
    data = Post.objects.filter(title__icontains=query)
    return render(request, 'blog_app/search.html', {"posts" : data})