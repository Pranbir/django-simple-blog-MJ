from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Comment, Post, Category
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import time
from . import tasks

# Create your views here.

#@login_required(login_url='/login/')
def index(request):
    data = Post.objects.order_by('-id')
    tasks.bekar.delay(5)
    return render(request, 'blog_app/home.html', {"posts" : data})

def contact(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        tasks.mail.delay(msg, name, email)
        a = "Successfully sent message"
        render(request, 'blog_app/contact.html', {"msg" : a})

    return render(request, 'blog_app/contact.html')

def single_post(request, id):
    data = Post.objects.get(id=id)
    comments =  Comment.objects.filter(post= data).select_related('author')
    return render(request, 'blog_app/single_post.html', {"post" : data , "comments": comments})


def search(request):
    query = request.GET['q']
    data = Post.objects.filter(title__icontains=query)
    return render(request, 'blog_app/search.html', {"posts" : data})


def add_comment(request, id):
    comment_body = request.POST.get('msg')
    comment_obj = Comment(post= Post.objects.get(id=id) , author=request.user , body = comment_body)
    comment_obj.save()
    return HttpResponseRedirect( reverse('blog_app:single_post', args=(id)) )


def author_post(request, id):
    data = Post.objects.filter(author = User.objects.get(id=id)).order_by('-id')
    return render(request, 'blog_app/home.html', {"posts" : data})


def login_user(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect( reverse('blog_app:index') )
    
    if request.method == 'GET':
        return render(request, 'blog_app/login.html')
    elif request.method == 'POST':
        username =  request.POST["username"]
        password =  request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect( reverse('blog_app:index') )
        else:
            msg = "Invalid Credential"
            return render(request, 'blog_app/login.html', {"msg" : msg})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect( reverse('blog_app:index') )
    
    if request.method == "GET":
        return render(request, 'blog_app/register.html')
    elif request.method=="POST":
        username =  request.POST["username"]
        email =  request.POST["email"]
        password =  request.POST["password"]

        if len(User.objects.filter(username=username)) != 0:
            msg = "Username Already Exists. Please use a different username."
            return render(request, 'blog_app/register.html', {"msg" : msg})

        user = User.objects.create_user(username,email, password)
        user.save()
        login(request, user)
        return HttpResponseRedirect( reverse('blog_app:index') )


def logout_user(request):
    logout(request)
    return HttpResponseRedirect( reverse('blog_app:index') )