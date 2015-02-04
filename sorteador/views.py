from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

# Create your views here.

def home(request, *args):
    return render_to_response('index.html')
