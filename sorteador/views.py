from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from sorteador.models import *


# Create your views here.

def home(request, *args):
    return render_to_response('index.html')

def new(request):
	data = {}
	data["jogadores"] = Jogador.objects.all()

	return render_to_response('new.html', data)
