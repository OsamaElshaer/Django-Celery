import django
from django import views


from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.test , name='test')
]
