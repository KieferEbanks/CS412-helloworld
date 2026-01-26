# file: django/hw/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import time # This is to show its a static website

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    '''A function that responds to the home request'''

    response_text = f'''
    <html>
        <h1>Hello, World!</h1>
        The current time is: { time.ctime() }.
    </html>
    '''

    return HttpResponse(response_text)
