from django import forms
#from transportes.forms import days
from .models import menus, ementas
from django.forms.widgets import Select

class NewMenuForm(forms.ModelForm):
	class Meta:
		model = menus
		fields = [
			'nome',
			'data',
			'precoAluno',
			'precoProfessor',
		]
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
			'data': forms.Select(attrs={'class': 'form-control'}),
			'precoAluno': forms.TextInput(attrs={'class': 'form-control'}),
			'precoProfessor': forms.TextInput(attrs={'class': 'form-control'}),
		}

class NewEmentaForm(forms.ModelForm):
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
			'menu':Select(attrs={'class': 'form-control'}),
			'sopa': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoCarne': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoPeixe': forms.TextInput(attrs={'class': 'form-control'}),
			'pratoVegetariano': forms.TextInput(attrs={'class': 'form-control'}),
			'sobremesa': forms.TextInput(attrs={'class': 'form-control'}),
		}