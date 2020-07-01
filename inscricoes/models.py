from django.db import models
from datetime import date
from atividades.models import sessao, atividades, sessoes
from utilizador.models import utilizador
from configuracoes.models import escolas, dias_DA, horas_transportes
from configuracoes.models import dias_DA 
# from almocos.models import ementas

class inscricao1(models.Model):

    class Group(models.TextChoices):
        Grupo_Escolar= 'Grupo Escolar', ('Grupo Escolar')
        Individual = 'Individual', ('Individual')

    PERCISA_TRANSPORTE = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    id = models.AutoField(primary_key=True)
    UtilizadorID = models.ForeignKey(utilizador,on_delete=models.CASCADE)
    Nome = models.CharField(max_length=200)
    Tipo_de_Visitante = models.CharField(max_length=50, choices=Group.choices)  
    Nr_Pessoas = models.IntegerField()   
    Escola = models.ForeignKey(escolas, on_delete=models.CASCADE)
    data = models.OneToOneField(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE)
    HorarioInicio = models.CharField(max_length=100)
    HorarioFim = models.CharField(max_length=100)
    Precisa_Transporte = models.CharField(verbose_name="Precisa transporte:", max_length=32, choices=PERCISA_TRANSPORTE,  default='Não')
    Refeicao = models.CharField(verbose_name="Precisa transporte:", max_length=32, choices=PERCISA_TRANSPORTE,  default='Não')
    Quantos_Alunos = models.IntegerField(blank=True, null= True)
    Quantos_Professores = models.IntegerField(blank=True, null= True)
    Observacoes = models.CharField(max_length=350, blank=True, null= True)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "inscricoes"
        db_table = "inscricoes"

    def __str__(self):
        return self.id  

class inscricao_atividades(models.Model):
    inscricaoID = models.ForeignKey(inscricao1, on_delete=models.CASCADE, blank= True, null = True)
    sessao = models.ForeignKey(sessao, verbose_name="Sessao:", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "inscricao_atividades"
        db_table = "inscricao_atividades_vieira"

#################################
################################# 
#############Daniel##############
#################################
#################################

class inscricoes(models.Model):
	CAMPUS = [
		('Gambelas', 'Gambelas'),
		('Penha', 'Penha'),
	]

	nome = models.CharField(max_length=200, unique=True)
	dias = models.ForeignKey(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE, blank=True, null=True)
	necessitaTransporte = models.BooleanField(default=True)
	horaInicio = models.ForeignKey(horas_transportes, verbose_name="Horas inicio transportes:", on_delete=models.CASCADE, related_name='horaFim')
	horaFim = models.ForeignKey(horas_transportes, verbose_name="Horas fim transportes:", on_delete=models.CASCADE, related_name='horaInicio')
	entreCampus = models.BooleanField(default=False)
	nParticipantes = models.IntegerField(verbose_name="Número de participantes:", default=1, blank=True, null=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name_plural = "inscricoes"
		db_table = "inscricoes_daniel"

class atividades_inscritas(models.Model):
	nome = models.ForeignKey(inscricoes, verbose_name="Grupo:", on_delete=models.CASCADE, blank=True, null=True) 
	atividade = models.ForeignKey(atividades, verbose_name="Atividade:", on_delete=models.CASCADE, blank=True, null=True)
	sessao = models.ForeignKey(sessoes, verbose_name="Sessoes:", on_delete=models.CASCADE, blank=True, null=True)
	
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name_plural = "atividades_inscritas"
		db_table = "atividades_inscritas_daniel"

