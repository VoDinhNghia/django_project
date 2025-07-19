from django.shortcuts import render
from django_app.models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from dotenv import load_dotenv
import os

def homePage(request):
    return render(request, "home.html", {"data": "test dd data"})

def createPost(request):
    return render(request, "create_new_post.html")

def createNewPost(request):
    return render(request, "home.html", {"data": "hello"})

def loginView(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def simpleUpload(request):
    load_dotenv()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'data': os.getenv("URL_HOST_LOCAL")+uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def handleImage():
    print('hande image upload')