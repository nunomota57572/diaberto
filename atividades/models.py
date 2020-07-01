from django.db import models
from datetime import date
from configuracoes.models import departamentos, uos
from utilizador.models import utilizador
from configuracoes.models import dias_DA, horas_atividades

class atividades(models.Model):
    CAMPUS = [
        ('Gambelas', 'Gambelas'),
        ('Penha', 'Penha'),
    ]

    nome = models.CharField(max_length=200, unique=True)
    campus = models.CharField(verbose_name="Campus:", max_length=32, choices=CAMPUS, default='Gambelas')
    vagas = models.IntegerField(default="1")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "atividades"
        db_table = "atividades_daniel"

class sessoes(models.Model):
    atividade = models.ForeignKey(atividades, verbose_name="Atividade:", on_delete=models.CASCADE, blank=True, null=True) 
    tempo = models.ForeignKey(horas_atividades, verbose_name="Horas atividades:", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "sessoes"
        db_table = "sessoes_daniel"

class atividade(models.Model):

    class ENUM(models.TextChoices):
        PENDENTE = 'Pendente', ('Pendente')
        ACEITE = 'aceite', ('Aceite')
        Rejeitado = 'rejeitado', ('Rejeitado')

    class Tipo(models.TextChoices):
        AtividadeLaboratorial = 'Atividade Laboratorial', ('Atividade Laboratorial')
        AtividadesTecnologicas = 'Atividades Tecnologicas', ('Atividades Tecnologicas')
        Debate = 'Debate', ('Debate')
        Palestra = 'Palestra', ('Palestra')
        Tertulia = 'Tertúlia', ('Tertulia')

    class TipoCampus(models.TextChoices):
        Gambelas = 'Gambelas', ('Gambelas')
        Penha = 'Penha', ('Penha')

    id = models.AutoField(primary_key=True)
    Nome_actividade = models.CharField(max_length=200, unique = True)
    Submetido = models.DateField(default=date.today)
    Estado = models.CharField(max_length=20,choices=ENUM.choices,default=ENUM.PENDENTE,)
    Criador = models.ForeignKey(utilizador, verbose_name="Criador:", on_delete=models.CASCADE, blank=True, null=True)
    Tipodeatividade = models.CharField(max_length=200,choices=Tipo.choices,)
    Descrição = models.CharField(max_length=20000)
    Campus = models.CharField(max_length=200,choices=TipoCampus.choices,)
    EntidadeOrganizacional = models.ForeignKey(uos, verbose_name="UO:", on_delete=models.CASCADE, blank=True, null=True)
    Departamento = models.ForeignKey(departamentos, verbose_name="Departamento:", on_delete=models.CASCADE, blank=True, null=True)
   

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "atividade"
        db_table = "atividades"

    def __str__(self):
        return self.Nome_actividade

class sessao(models.Model):

    id = models.AutoField(primary_key=True)
    Dia = models.ForeignKey(dias_DA, verbose_name="Dia:", on_delete=models.CASCADE, blank=True, null=True)
    Inicio = models.ForeignKey(horas_atividades, verbose_name="Horas atividades:", on_delete=models.CASCADE)
    Duraçao = models.IntegerField(default="1")
    Vagas = models.IntegerField(default="1")
    Espaço = models.CharField(max_length=200)
    Materiais= models.CharField(max_length=20000)
    Colaboradores = models.IntegerField()
    Atividade = models.ForeignKey(atividade, verbose_name="Atividade:", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "sessao"
        db_table = "sessao"

    def __str__(self):
        return str(self.id)