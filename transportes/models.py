from django.db import models
from datetime import datetime
from configuracoes.models import horas_transportes, dias_DA
 
class autocarros(models.Model):
	identificador = models.CharField(verbose_name="Identificador do autocarro:", max_length=32, unique=True, error_messages={'unique':"Este autocarro já foi registado"})
	capacidade = models.IntegerField(verbose_name="Capacidade máxima:", default=1)
	
	def __str__(self):
		return self.identificador

	class Meta:  
		verbose_name_plural = "Autocarros"
		db_table = "autocarros"

class percursos(models.Model):
	PERCURSOS = [
		('Faro', 'Faro'),
		('Gambelas', 'Gambelas'),
		('Penha', 'Penha'),
	]

	identificador = models.ForeignKey(autocarros, verbose_name="ID do Autocarro:", on_delete=models.CASCADE, blank=True, null=True) 
	dias = models.ForeignKey(dias_DA, verbose_name="Dias:", on_delete=models.CASCADE, blank=True, null=True)
	origem = models.CharField(verbose_name="Origem:", max_length=32, choices=PERCURSOS,  default='Faro')
	destino = models.CharField(verbose_name="Destino:", max_length=32, choices=PERCURSOS,  default='Gambelas')
	horario = models.ForeignKey(horas_transportes, verbose_name="Horas:", on_delete=models.CASCADE, blank=True, null=True)
	lotacao = models.IntegerField(verbose_name="Lotação:", default=0, blank=True, null=True)
	lugares_restantes = models.IntegerField(verbose_name="Lugares restantes:", default=10, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Percursos"
		db_table = "percursos"