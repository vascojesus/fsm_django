from django.db import models

# Create your models here.


class Automato(models.Model):
    descricao = models.CharField(max_length=70)
    estados = models.CharField(max_length=30)
    alfabeto = models.CharField(max_length=10)
    estado_inicial = models.CharField(max_length=1)
    estados_aceitacao = models.CharField(max_length=10)
    tabela_transicao = models.CharField(max_length=30)

class Maquina(models.Model):
    descricao = models.CharField(max_length=70)
    estados = models.CharField(max_length=30)
    alfabeto = models.CharField(max_length=10)
    alfabeto_fita = models.CharField(max_length=10)
    estado_inicial = models.CharField(max_length=1)
    halt_accept = models.CharField(max_length=10)
    halt_reject = models.CharField(max_length=10)
    tabela_transicao = models.CharField(max_length=30)

class Sequencia(models.Model):
    sequencia = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao
