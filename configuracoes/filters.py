import django_filters
from .models import escolas, uos, departamentos, cursos
from django import forms


class FilterEscolas(django_filters.FilterSet):
	nome = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = escolas
		fields = [
			'nome',
		]
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
		}

class FilterUO(django_filters.FilterSet):
	sigla = django_filters.CharFilter(lookup_expr='icontains')
	nome = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = uos
		fields = [
			'sigla',
			'nome',
		]
		widgets = {
			'sigla': forms.TextInput(attrs={'class': 'form-control'}),
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
		}

class FilterDepartamento(django_filters.FilterSet):
	departamento = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = departamentos
		fields = [
			'uo',
			'departamento',
		]
		widgets = {
			'uo': forms.TextInput(attrs={'class': 'form-control'}),
			'departamento': forms.TextInput(attrs={'class': 'form-control'}),
		}

class FilterCurso(django_filters.FilterSet):
	sigla = django_filters.CharFilter(lookup_expr='icontains')
	nome = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = cursos
		fields = [
			'sigla',
			'nome',
		]
		widgets = {
			'sigla': forms.TextInput(attrs={'class': 'form-control'}),
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
		}