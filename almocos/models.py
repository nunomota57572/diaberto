from django.db import models
from datetime import datetime 
from configuracoes.models import dias_DA 

class menus(models.Model):
    nome = models.CharField(verbose_name="Nome:", max_length=32, unique=True, error_messages={'unique':"Já foi registado um menu com este nome"})
    data = models.OneToOneField(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE, unique=True, error_messages={'unique':"Já foi registado um menu para este dia"})
    precoAluno = models.DecimalField(verbose_name="Preço por aluno:", max_digits=3, decimal_places=2, default='2.70')
    precoProfessor = models.DecimalField(verbose_name="Preço por professor:", max_digits=3, decimal_places=2, default='4.20')

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural = "Menu"
        db_table = "menu"

class ementas(models.Model):
    menu = models.OneToOneField(menus, verbose_name="Menu:", on_delete=models.CASCADE, unique=True, error_messages={'unique':"Já foi registado uma ementa para este menu"})
    sopa = models.CharField(verbose_name="Sopa:", max_length=32)
    pratoCarne = models.CharField(verbose_name="Prato de carne:", max_length=32)
    pratoPeixe = models.CharField(verbose_name="Prato de peixe:", max_length=32)
    pratoVegetariano = models.CharField(verbose_name="Prato vegetariano:", max_length=32)
    sobremesa = models.CharField(verbose_name="Sobremesa:", max_length=32)
    
    class Meta:
        verbose_name_plural = "Ementa"
        db_table = "ementa"