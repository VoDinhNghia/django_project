from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from dotenv import load_dotenv
import os
load_dotenv()

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'data': os.getenv("URL_HOST_LOCAL")+uploaded_file_url
        })
    return render(request, 'simple_upload.html')