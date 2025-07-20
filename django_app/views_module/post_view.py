from django.shortcuts import render

def create_post(request):
    return render(request, "create_new_post.html")

def create_new_post(request):
    return render(request, "home.html", {"data": "hello"})