from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    
    path('normalsendemails' , views.send_mails , name='sendmails'),
    path('schedulsendmails' , views.schedulsend_mails , name='schedulsendmails')
]
