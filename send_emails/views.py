from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_emails
# Create your views here.


def send_mails(request):
    send_emails.delay()
    return HttpResponse('Sent')