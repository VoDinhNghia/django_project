from django.shortcuts import render
from django_app.models import Post

def homePage(request):
    return render(request, "home.html", {"data": "test data"})

def createPost(request):
    return render(request, "createNewPost.html")

def createNewPost(request):
    print("test call api")
    return render(request, "home.html", {"data": "hello"})