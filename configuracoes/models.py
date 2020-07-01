from django.db import models
from datetime import date 

class main(models.Model): 
    today = date.today() 

    endereçoPaginaWeb = models.CharField(max_length=200, verbose_name="URL:")
    emailDiaAberto = models.EmailField(verbose_name="Email:")
    ano = models.IntegerField(verbose_name="Ano:", default=today.year, unique=True, error_messages={'unique':"Já foram criadas configurações para este ano"})
    
    dataPropostasAtividadesIncio = models.DateField(verbose_name="Início:")
    dataPorpostaAtividadesFim = models.DateField(verbose_name="Fim:")

    dataInscriçãoAtividadesInicio = models.DateField(verbose_name="Início:")
    dataInscriçãoAtividadesFim = models.DateField(verbose_name="Fim:")

    dataDiaAbertoInicio = models.DateField(verbose_name="Início:")
    dataDiaAbertoFim = models.DateField(verbose_name="Fim:")

    descrição = models.TextField()
     
    class Meta:
        verbose_name_plural = "Configurações gerais"
        db_table = "configuracoes_gerais"

class dias_DA(models.Model):
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.data
        
    class Meta:
        verbose_name_plural = "Dias do Dia Aberto"
        db_table = "dias_Dia_aberto"

class horarios_transportes(models.Model):
    inicio = models.IntegerField(verbose_name="Início:", default=0)
    fim = models.IntegerField(verbose_name="Fim:", default=0)
    periodo = models.IntegerField(verbose_name="Periodo:", default=1)

    class Meta:  
        verbose_name_plural = "Horarios Transportes"
        db_table = "horarios_transportes"

class horarios_atividades(models.Model):
    inicio = models.IntegerField(verbose_name="Início:", default=0)
    fim = models.IntegerField(verbose_name="Fim:", default=0)
    periodo = models.IntegerField(verbose_name="Periodo:", default=1)

    class Meta:  
        verbose_name_plural = "Horarios Atividades"
        db_table = "horarios_atividades"

class horas_transportes(models.Model):
    tempo = models.TimeField()
    def __str__(self):
        return self.tempo.strftime("%H:%M")
        
    class Meta:  
        verbose_name_plural = "Horas dos transportes"
        db_table = "horas_transportes"

class horas_atividades(models.Model):
    tempo = models.TimeField()
    def __str__(self):
        return self.tempo.strftime("%H:%M")
        
    class Meta:  
        verbose_name_plural = "Horas das atividades"
        db_table = "horas_atividades"

class escolas(models.Model):
    
    nome = models.CharField(max_length=200, verbose_name="Nome:", unique=True, error_messages={'unique':"Esta escola já foi registada"})
    
    def __str__(self):
        return self.nome

    class Meta:  
        db_table = "escolas"

class uos(models.Model):
    sigla = models.CharField(max_length=200, verbose_name="Sigla:", default="", unique=True, error_messages={'unique':"A sigla desta Unidade Orgânica já foi registada"})
    nome = models.CharField(max_length=200, verbose_name="Nome:", unique=True, error_messages={'unique':"O nome desta Unidade Orgânica já foi registado"})
    class Meta:  
        db_table = "uo"
    def __str__(self):
        return self.sigla

class departamentos(models.Model):
    uo = models.ForeignKey(uos, verbose_name="Unidade Organica:", on_delete=models.CASCADE, blank=True, null=True)
    departamento = models.CharField(max_length=200, verbose_name="Departamento:", unique=True, error_messages={'unique':"O nome deste Departamento já foi registado"})
    class Meta:  
        db_table = "departamentos"
    def __str__(self):
        return self.departamento

class cursos(models.Model):
    sigla = models.CharField(max_length=200, verbose_name="Sigla:", unique=True, error_messages={'unique':"A sigla deste Curso já foi registada"})
    nome = models.CharField(max_length=200, verbose_name="Nome:", unique=True, error_messages={'unique':"O nome deste Curso já foi registado"})
    class Meta:  
        db_table = "cursos"
    def __str__(self):
        return self.sigla