from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='test_view')
]