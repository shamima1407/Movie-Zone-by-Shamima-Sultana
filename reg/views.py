from django.shortcuts import render
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from home import *


@csrf_protect
def registration(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post=Post()
            post.email= request.POST.get('email')
            post.password= request.POST.get('password')
            post.save()
                
            return render(request, 'reg/login.html')  

    else:
        return render(request,'reg/registration.html')
            

@csrf_protect
def login(request):
    if request.method == 'POST':
        if Post.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            member = Post.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'reg/msg.html')
        else:
            
            return render(request, 'reg/error.html')
    else:
        return render(request,'reg/login.html')

def msg(request):
    return render(request,'reg/msg.html')

def error(request):
    return render(request,'reg/error.html')

