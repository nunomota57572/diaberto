import django_filters
from .models import ementas
from django import forms

class FilterEmentas(django_filters.FilterSet):
	class Meta:
		model = ementas
		fields = [
			'menu',
			'sopa',
			'pratoCarne',
			'pratoPeixe',
			'pratoVegetariano',
			'sobremesa',
		]
		widgets = {
			'menu': forms.TextInput(attrs={'class': 'form-control'}),
			'sopa': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoCarne': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoPeixe': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoVegetariano': forms.TextInput(attrs={'class': 'form-control'}),
			'sobremesa': forms.TextInput(attrs={'class': 'form-control'}),
		}