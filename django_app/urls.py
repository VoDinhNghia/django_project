from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-view'),
    path('create-post', views.createPost, name='create-post'),
    path('api-create-post', views.createNewPost, name='api-create-post'),
    path('simple-upload', views.simpleUpload, name='simple-upload')
]