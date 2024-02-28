from django.urls import path
from django.http import HttpResponse
from library.views import home

urlpatterns = [
    path("", home, name='home')
]