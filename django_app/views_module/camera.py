from django.shortcuts import render

def camera_page(request):
    return render(request, "camera/open_camera.html")