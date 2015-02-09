#-*- coding: utf-8 -*-
from django.db import models

class Jogador(models.Model):
	nome = models.CharField(max_length=100)
	apelido = models.CharField(null=True, max_length=100)
	eh_diretoria = models.BooleanField(default=False)
	foto = models.ImageField(upload_to="atletas/", null=True, blank=True)

	def __unicode__(self):
		return u"%s" % (self.nome)

class Equipe(models.Model):
	data_criacao = models.DateField(auto_now=True)
	nome = models.CharField(max_length=100)
	cabeca = models.ForeignKey("Jogador", null=True, related_name="cabeca")
	anticabeca = models.ForeignKey("Jogador", null=True, related_name="anticabeca")
	aspira = models.ForeignKey("Jogador", null=True, related_name="aspira")
	normais = models.ManyToManyField(Jogador, null=True, related_name="normais")

	def __unicode__(self):
		return u"%s - %s" % (self.nome, self.data_criacao)

class Sorteio(models.Model):
	data_criacao = models.DateTimeField(auto_now=True)
	equipes = models.ManyToManyField(Equipe, null=True, blank=True)

