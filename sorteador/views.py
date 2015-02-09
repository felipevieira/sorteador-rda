from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from sorteador.models import *

import datetime


import random

# Create your views here.

def home(request, *args):
	data = {}
	#sorteio = Sorteio.objects.order_by('-pk')[0]
	#data["campinense"] = sorteio.equipes.filter(nome="Campinense")[0]
	#data["treze"] = sorteio.equipes.filter(nome="Treze")[0]
	#data["atletico"] = sorteio.equipes.filter(nome="Atletico de Cajazeiras")[0]
	#data["nacional"] = sorteio.equipes.filter(nome="Nacional de Patos")[0]

	#date = sorteio.data_criacao - datetime.timedelta(hours=3)
	#data["data_criacao"] = date.strftime("%d/%m/%y - %H:%M")

	return render_to_response('index.html', data, context_instance=RequestContext(request))


def new(request):
	data = {}
	data["jogadores"] = Jogador.objects.all()

	return render_to_response('new.html', data, context_instance=RequestContext(request))

def sortear(request):
	cabecas = request.POST.getlist("cabecas")
	antis = request.POST.getlist("anti")
	aspiras = request.POST.getlist("aspiras")
	outros = request.POST.getlist("outros")

	campinense = Equipe()
	campinense.nome = "Campinense"
	campinense.save()

	atletico = Equipe()
	atletico.nome = "Atletico de Cajazeiras"
	atletico.save()

	nacional = Equipe()
	nacional.nome = "Nacional de Patos"
	nacional.save()

	treze = Equipe()
	treze.nome = "Treze"
	treze.save()

	equipes = [campinense,atletico,nacional,treze]

	sortear_categoria(equipes, cabecas, tipo="cabeca")
	sortear_categoria(equipes, antis, tipo="anticabeca")
	sortear_categoria(equipes, aspiras, tipo="aspira")
	sortear_categoria(equipes, outros, tipo="normal")
	sortear_categoria(equipes, outros, tipo="normal")

	sorteio = Sorteio()
	sorteio.save()
	sorteio.equipes.add(campinense)
	sorteio.equipes.add(atletico)
	sorteio.equipes.add(nacional)
	sorteio.equipes.add(treze)
	sorteio.save()

	data = {}
	data["campinense"] = campinense
	data["treze"] = treze
	data["atletico"] = atletico
	data["nacional"] = nacional

	return render_to_response('index.html', data, context_instance=RequestContext(request))

def sortear_categoria(equipes, atletas, tipo="normal"):
	for equipe in equipes:
		if possui_diretor(equipe):
			index = random.randint(0, len(atletas)-1)
			escolhido = Jogador.objects.get(nome=str(atletas[index]))
			while escolhido.eh_diretoria:
				index = random.randint(0, len(atletas)-1)
				escolhido = Jogador.objects.get(nome=str(atletas[index]))
			del(atletas[index])
			if tipo == "normal":
				equipe.normais.add(escolhido)
				equipe.save()
			elif tipo == "cabeca":
				equipe.cabeca = escolhido
				equipe.save()
			elif tipo == "anticabeca":
				equipe.anticabeca = escolhido
				equipe.save()
			elif tipo == "aspira":
				equipe.aspira = escolhido
				equipe.save()
		else:
			index = random.randint(0, len(atletas)-1)
			atleta = Jogador.objects.get(nome=str(atletas[index]))
			del(atletas[index])
			if tipo == "normal":
				equipe.normais.add(atleta)
				equipe.save()
			elif tipo == "cabeca":
				equipe.cabeca = atleta
				equipe.save()
			elif tipo == "anticabeca":
				equipe.anticabeca = atleta
				equipe.save()
			elif tipo == "aspira":
				equipe.aspira = atleta
				equipe.save()

def possui_diretor(equipe):
	if equipe.cabeca and equipe.cabeca.eh_diretoria:
		return True
	elif equipe.anticabeca and equipe.anticabeca.eh_diretoria:
		return True
	elif equipe.aspira and equipe.aspira.eh_diretoria:
		return True
	for atleta in equipe.normais.all():
		if atleta.eh_diretoria:
			return True
	return False

