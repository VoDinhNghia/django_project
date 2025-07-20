from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-view'),
    path('create-post', views.create_post, name='create-post'),
    path('api-create-post', views.create_new_post, name='api-create-post'),
    path('simple-upload', views.simple_upload, name='simple-upload'),
    path('resize-img', views.resize_img, name='resize-img'),
    path('view-camera-page', views.camera_page, name='view-camera-page')
]