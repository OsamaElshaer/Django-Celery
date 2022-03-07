from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    
    path('' , views.send_mails , name='sendmails')
]
