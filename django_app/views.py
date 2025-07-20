from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .views_module.simple_upload_view import *
from .views_module.post_view import *
from .views_module.handle_image_view import *

def home_page(request):
    return render(request, "home.html", {"data": "test dd data"})