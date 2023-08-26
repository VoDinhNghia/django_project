from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='test_view'),
    path('create-post', views.createPost, name='create-post'),
    path('api-create-post', views.createNewPost, name='api-create-post')
]