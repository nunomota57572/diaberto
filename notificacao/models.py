from django.db import models
from utilizador.models import utilizador
from datetime import datetime 


class Notificacao(models.Model):
    assunto = models.CharField(db_column='Assunto', max_length=100)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao',  blank=True, null=True)  # Field name made lowercase.
    criadoem = models.DateTimeField(default=datetime.now, db_column='CriadoEm', blank=True)  # Field name made lowercase.
    autorid = models.ForeignKey(utilizador, on_delete=models.CASCADE, related_name='autorid',db_column='autorID', blank=True, null=True)  # Field name made lowercase.
    remetenteid = models.ForeignKey(utilizador, on_delete=models.CASCADE,verbose_name= 'Destinatário', related_name='remetenteid',  db_column='remetenteID', blank=True, null=True)  # Field name made lowercase.
    is_read = models.BooleanField(db_column='is_Read', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        db_table = 'notificacao'


