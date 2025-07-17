from django.shortcuts import render
from django_app.models import Post
from django.contrib.auth.forms import AuthenticationForm

def homePage(request):
    return render(request, "home.html", {"data": "test data"})

def createPost(request):
    return render(request, "create_new_post.html")

def createNewPost(request):
    print("test call api")
    return render(request, "home.html", {"data": "hello"})

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})