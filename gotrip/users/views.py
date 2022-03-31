from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'users/home.html')
def register(request):
    return render(request, 'users/register.html')
