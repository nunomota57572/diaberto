import django_filters
from .models import percursos, autocarros
from django.forms.widgets import Select
from django import forms

class FilterAutocarro(django_filters.FilterSet):
	class Meta:
		model = autocarros
		fields = '__all__'

class FilterPercurso(django_filters.FilterSet):
	class Meta:
		model = percursos
		fields = '__all__'
		widgets = {
			'identificador': Select(attrs={'class': 'form-control'}),
			'dias': forms.TextInput(attrs={'class': 'form-control'}),
			'origem': Select(attrs={'class': 'form-control'}),
			'destino': Select(attrs={'class': 'form-control'}),
			'horario': forms.TextInput(attrs={'class': 'form-control'}),
			'lotacao': forms.TextInput(attrs={'class': 'form-control'}),
		}