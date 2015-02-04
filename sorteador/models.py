#-*- coding: utf-8 -*-
from django.db import models

class Jogador(models.Model):
	nome = models.CharField(max_length=100)
	apelido = models.CharField(null=True, max_length=100)
	eh_diretoria = models.BooleanField(default=False)
	foto = models.ImageField(upload_to="atletas/", null=True)

	def __unicode__(self):
		return u"%s" % (self.nome)

class Equipe(models.Model):
	nome = models.CharField(max_length=100)
	integrantes = models.ManyToManyField(Jogador)

class Sorteio(models.Model):
	data_criacao = models.DateField(auto_now=True)
	equipes = models.ManyToManyField(Equipe)

