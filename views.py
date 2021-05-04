from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from bloghome.forms import CustomUserCreationForm


def homepage(request):
    return render(request, 'bloghome/homepage.html')

def register(request):
    if request.method == 'GET':
        return render(
            request, 'bloghome/register.html',
            {"form": CustomUserCreationForm} 
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.comtrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
        return render(request, 'bloghome/homepage.html')
        
