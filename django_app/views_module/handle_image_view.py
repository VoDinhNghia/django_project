from django.shortcuts import render
from PIL import Image
from dotenv import load_dotenv
import os
load_dotenv()

def resize_img(request):
    if request.method == 'POST':
        url_img = request.body
        img = Image.open(url_img.replace(os.getenv("URL_HOST_LOCAL"), ''))
        img.show()
        return 0
    return 0