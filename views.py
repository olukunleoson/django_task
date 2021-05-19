from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from bloghome.forms import CommentForm, UserCreationForm
from bloghome import models



def homepage(request):
    return render(request, 'bloghome/homepage.html')

def contact(request):
    return render(request, 'bloghome/contact.html')
    

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.post = register
            user.save()
            login(user.username)
        return render(request, 'bloghome/homepage.html')
    
    elif request.method == 'GET':
        return render(request, 'bloghome/register.html', {"form": UserCreationForm})

def login(request, user):
        return render(request, 'bloghome/login.html')

def Post(request):
    return render(request, 'bloghome/post.html')   

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "Post":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bloghome/post.html', {'form': form})
