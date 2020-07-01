from django import forms
from .models import main, horarios_transportes, horarios_atividades, escolas, departamentos, cursos, uos

class NewGeralForm(forms.ModelForm):
	class Meta:
		model = main
		fields = (
			'endereçoPaginaWeb',
			'emailDiaAberto',
			'ano',
			'dataPropostasAtividadesIncio',
			'dataPorpostaAtividadesFim',
			'dataInscriçãoAtividadesInicio',
			'dataInscriçãoAtividadesFim', 
			'dataDiaAbertoInicio',
			'dataDiaAbertoFim',
			'descrição',
		)
		widgets = {
				'endereçoPaginaWeb': forms.TextInput(attrs={'class': 'form-control'}),
				'emailDiaAberto': forms.TextInput(attrs={'class': 'form-control'}),
				'ano': forms.TextInput(attrs={'class': 'form-control'}),
				'descrição': forms.Textarea(attrs={'class': 'form-control'}),
		}
		
	def clean(self):
		cleaned_data = super(NewGeralForm, self).clean()
		p_i = self.cleaned_data.get('dataPropostasAtividadesIncio')
		p_f = self.cleaned_data.get('dataPorpostaAtividadesFim')
		i_i = self.cleaned_data.get('dataInscriçãoAtividadesInicio')
		i_f = self.cleaned_data.get('dataInscriçãoAtividadesFim')
		d_i = self.cleaned_data.get('dataDiaAbertoInicio')
		d_f = self.cleaned_data.get('dataDiaAbertoFim')
		if p_f < p_i:
			raise forms.ValidationError('Data inicial de propor atividades não pode ser superior à final')
		if i_i < p_f:
			raise forms.ValidationError('Data final de propor atividades não pode ser superior à inicial das inscrições')
		if i_f < i_i:
			raise forms.ValidationError('Data inicial das inscrições não pode ser superior à final')
		if d_i < i_f:
			raise forms.ValidationError('Data final das inscrições não pode ser superior à inicial do Dia Abeto')
		if d_f < d_i:
			raise forms.ValidationError('Data inicial do Dia Aberto não pode ser superior à final')
	
class NewHorarioTransporteForm(forms.ModelForm):
	class Meta: 
		model = horarios_transportes
		fields = [
			'inicio',
			'fim',
			'periodo',
		]
		widgets = {
			'inicio': forms.NumberInput(attrs={'min':0, 'max':23, 'class': 'form-control', 'style': 'width: 100px;', 'label_suffix':'horas'}),
			'fim': forms.NumberInput(attrs={'min':0, 'max':23, 'class': 'form-control', 'style': 'width: 100px'}), 
			'periodo': forms.NumberInput(attrs={'min':1, 'max':60, 'class': 'form-control', 'style': 'width: 100px'}),
		}
	def clean(self):
		cleaned_data = super(NewHorarioTransporteForm, self).clean()
		inicio = self.cleaned_data.get('inicio')
		fim = self.cleaned_data.get('fim')  
		if inicio > fim:
			raise forms.ValidationError('O Fim tem que ser depois do Início.')
		return cleaned_data

class NewHorarioAtividadeForm(forms.ModelForm):
	class Meta: 
		model = horarios_atividades
		fields = [
			'inicio',
			'fim',
			'periodo',
		]
		widgets = {
			'inicio': forms.NumberInput(attrs={'min':0, 'max':23, 'class': 'form-control', 'style': 'width: 100px;', 'label_suffix':'horas'}),
			'fim': forms.NumberInput(attrs={'min':0, 'max':23, 'class': 'form-control', 'style': 'width: 100px'}), 
			'periodo': forms.NumberInput(attrs={'min':1, 'max':60, 'class': 'form-control', 'style': 'width: 100px'}),
		}
	def clean(self):
		cleaned_data = super(NewHorarioAtividadeForm, self).clean()
		inicio = self.cleaned_data.get('inicio')
		fim = self.cleaned_data.get('fim')  
		if inicio > fim:
			raise forms.ValidationError('O Fim tem que ser depois do Início.')
		return cleaned_data


class NewEscolaForm(forms.ModelForm):
	class Meta:
		model = escolas
		fields = [
			'nome',
		]
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control'}),
		}

class NewUOForm(forms.ModelForm):
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

class NewDepartamentoForm(forms.ModelForm):
	class Meta:
		model = departamentos
		fields = [
			'uo',
			'departamento',
		]
		widgets = {
			'uo': forms.Select(attrs={'class': 'form-control', 'required': True}),
			'departamento': forms.TextInput(attrs={'class': 'form-control'}),
		}

class NewCursoForm(forms.ModelForm):
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