from django import forms
from datetime import datetime, date, timedelta
from .models import autocarros, percursos
from configuracoes.models import main, horarios_transportes
from django.forms.widgets import Select

class NewAutocarroForm(forms.ModelForm):
	class Meta: 
		model = autocarros
		fields = [
			'identificador', 
			'capacidade', 
		] 
		widgets = {
			'identificador': forms.TextInput(attrs={'class': 'form-control'}),
			'capacidade': forms.TextInput(attrs={'class': 'form-control'}),
		}
 
class NewPercursoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.autocarro = kwargs.pop('autocarro', None)
		super().__init__(*args, **kwargs)

	class Meta:
		model = percursos
		fields = [
			'identificador',
			'dias',
			'origem', 
			'destino', 
			'horario',
			'lotacao',
			'lugares_restantes',
		]
		widgets = {
			'origem':Select(attrs={'class': 'form-control', 'required': True}),
			'destino':Select(attrs={'class': 'form-control', 'required': True}),
			'dias': forms.Select(attrs={'class': 'form-control', 'required': True}),
			'horario': forms.Select(attrs={'class': 'form-control', 'required': True}),
		}
	def clean(self):
		cleaned_data = super(NewPercursoForm, self).clean()
		origem = self.cleaned_data.get('origem')
		destino = self.cleaned_data.get('destino')
		dias = self.cleaned_data.get('dias')
		horario = self.cleaned_data.get('horario')
		if percursos.objects.filter(identificador=self.autocarro, dias=dias, horario=horario).exists():
			raise forms.ValidationError('Já foi atribuido um percurso para este autocarro neste horário.')
		if origem == destino:
			raise forms.ValidationError('A origem tem de ser diferente do destino.')

class NewEditPercursoForm(forms.ModelForm):
	class Meta:
		model = percursos
		fields = [
			'identificador',
			'dias',
			'origem', 
			'destino', 
			'horario',
			'lotacao',
			'lugares_restantes',
		]
		widgets = {
			'identificador':Select(attrs={'class': 'form-control', 'required': True}),
			'origem':Select(attrs={'class': 'form-control', 'required': True}),
			'destino':Select(attrs={'class': 'form-control', 'required': True}),
			'dias':Select(attrs={'class': 'form-control', 'required': True}),
			'horario':Select(attrs={'class': 'form-control', 'required': True}),
		}
'''
	def clean(self):
		cleaned_data = super(NewEditPercursoForm, self).clean()
		dias = self.cleaned_data.get('dias')
		percurso = self.cleaned_data.get('percurso')
		horario = self.cleaned_data.get('horario')
		if percursos.objects.filter(dias=dias, percurso=percurso, horario=horario).exists():
			raise forms.ValidationError('Este percurso um percurso para este horário neste autocarro.')
'''

