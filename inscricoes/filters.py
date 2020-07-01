import django_filters
from .models import inscricao1, inscricao_atividades
from atividades.models import atividade
from django.forms.widgets import Select
from django import forms


class FilterInscricao1(django_filters.FilterSet):
	class Meta:
		model = inscricao1
		fields = '__all__'
		widgets = {
			'Nome': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipo_de_Visitante': Select(attrs={'class': 'form-control'}),
            'Escola': Select(attrs={'class': 'form-control'}),
			'data': Select(attrs={'class': 'form-control'}),
			'Precisa_Transporte': Select(attrs={'class': 'form-control'}),
            'Refeicao': Select(attrs={'class': 'form-control'}),
		}

class FilterAtividades(django_filters.FilterSet):
	class Meta:
		model = atividade
		fields = '__all__'
		widgets = {
			'Nome_actividade': forms.TextInput(attrs={'class': 'form-control'}),
			'EntidadeOrganizacional': Select(attrs={'class': 'form-control'}),
			'Departamento': Select(attrs={'class': 'form-control'}),
			'Campus': Select(attrs={'class': 'form-control'}),
			'Tipodeatividade': Select(attrs={'class': 'form-control'}),
		}