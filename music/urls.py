from django.urls import path
#import the views module from music directory.
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
]