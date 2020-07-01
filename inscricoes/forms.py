from django import forms
from datetime import datetime, date, timedelta
from configuracoes.models import main
from .models import inscricao1, inscricao_atividades
from django.forms.widgets import Select

class NewInscricaoForm(forms.ModelForm):
	
	class Meta:
		model = inscricao1
		fields = [
			"id",
			"Nome",
			"Tipo_de_Visitante", 
			"Nr_Pessoas", 
			"Escola", 
			'data',
			"HorarioInicio", 
			"HorarioFim", 
			"Precisa_Transporte",
			"Refeicao", 
			"Quantos_Alunos",
			"Quantos_Professores" 
		]
		widgets = {
			'Nome': forms.TextInput(attrs={'class': 'form-control'}),
			'Tipo_de_Visitante': forms.Select(attrs={'class': 'form-control'}),
			'Nr_Pessoas': forms.NumberInput(attrs={'min':1, 'class': 'form-control'}),
			'Escola': forms.Select(attrs={'class': 'form-control'}),
			'data': forms.Select(attrs={'class': 'form-control'}),
			'HorarioInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
			'HorarioFim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
			'Precisa_Transporte': forms.Select(attrs={'class': 'form-control'}),
			'Refeicao': forms.Select(attrs={'class': 'form-control'}),
			'Quantos_Alunos': forms.NumberInput(attrs={'min':1, 'class': 'form-control'}), 
			'Quantos_Professores': forms.NumberInput(attrs={'min':1, 'class': 'form-control'}),
		}

class NewInscricaoForm1(forms.ModelForm):
	class Meta:
		model = inscricao_atividades
		fields = [
			'inscricaoID',
			'sessao'
		]
		widgets = {
			'sessao' : forms.Textarea(attrs={'class': 'form-control'}),
		}

class NewEditInscricaoForm(forms.ModelForm):
	class Meta:
		model = inscricao1
		fields = [
			"Nome",
			"Tipo_de_Visitante", 
			"Nr_Pessoas", 
			"Escola", 
			'data',
			"HorarioInicio", 
			"HorarioFim", 
			"Precisa_Transporte",
			"Refeicao", 
			"Quantos_Alunos",
			"Quantos_Professores",
			"Observacoes",
		]
		widgets = {
			'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipo_de_Visitante': forms.Select(attrs={'class': 'form-control'}),
            'Nr_Pessoas': forms.NumberInput(attrs={'min':1, 'class': 'form-control'}),
            'Escola': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.Select(attrs={'class': 'form-control'}),
            'HorarioInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'HorarioFim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Precisa_Transporte': forms.Select(attrs={'class': 'form-control'}),
            'Refeicao': forms.Select(attrs={'class': 'form-control'}),
            'Quantos_Alunos': forms.NumberInput(attrs={'min':0, 'class': 'form-control'}), 
            'Quantos_Professores': forms.NumberInput(attrs={'min':0, 'class': 'form-control'}),
            'Observacoes': forms.TextInput(attrs={'class': 'form-control'}),
		}