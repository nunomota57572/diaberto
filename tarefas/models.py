from django.db import models
from utilizador.models import *
from configuracoes.models import dias_DA
from atividades.models import atividade as actividade
# Create your models here.

from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
# Create your models here.

TITLE_CHOICES = [
    ('Atividade', 'Atividade'),
    ('Acompanhar participantes', 'Acompanhar participante'),
    ('Outro', 'Outro'),
]


class tarefa(models.Model):
    UtilizadorID2 = models.ForeignKey(colab, on_delete=models.CASCADE, blank=True, null=True)
    UtilizadorID = models.ForeignKey(coord,on_delete=models.CASCADE)
    Nome = models.CharField(max_length=200)
    Dia = models.ForeignKey(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE, blank=True, null=True)
    Concluida = models.IntegerField(default=0)
    HorasInicio = models.TimeField(blank = False)
    HorasFim = models.TimeField(blank = False)
    Tipo = models.CharField(max_length=24, choices=TITLE_CHOICES)
    Origem = models.CharField(max_length=200,default=None,blank=True)
    Destino = models.CharField(max_length=200,default=None,blank=True)
    Grupos = models.IntegerField()
    Descricao = models.TextField(blank=True)
    Nome_actividade = models.ForeignKey(actividade, on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "tarefa"

class disponibilidade(models.Model):
    UtilizadorID = models.ForeignKey(utilizador, verbose_name="UtilizadorID", on_delete=models.CASCADE, blank=True, null=True)
    Dia = models.ForeignKey(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE, blank=True, null=True)
    Inicio = models.TimeField(blank = False)
    Fim = models.TimeField(blank = False)
    Observacoes = models.TextField(blank = True)
    def __int__(self):
        return self.Id
