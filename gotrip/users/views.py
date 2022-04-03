import requests
from django.shortcuts import render, redirect
from django.http.response import  HttpResponse
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'users/home.html')
def register(request):
    if request.method == 'post':
        form=UserCreationForm(requests.post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
def base(request):
    if request.method == 'post':
        form = UserCreationForm(requests.post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/base.html', {'form':form})
def login(request):
    return render(request, 'users/Login.html')