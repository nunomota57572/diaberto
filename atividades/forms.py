from django import forms
from .models import atividade
from .models import sessao


class NewAtividadeForm(forms.ModelForm):
    #Nome
    #Submetido
    #Estado
    #Criador
    #Tipodeatividade
    #Descrição
    #Campus
    #EntidadeOrganizacional
    #Departamento
    class Meta:
        model = atividade
        fields = ["Nome_actividade","Tipodeatividade","Descrição","Campus"]
        widgets = {
            'Nome_actividade': forms.TextInput(attrs={'class': 'form-control'}),
            'Tipodeatividade': forms.Select(attrs={'class': 'form-control'}),
            'Descrição': forms.Textarea(attrs={'class': 'form-control'}),
            'Campus': forms.Select(attrs={'class': 'form-control'}),

        }


class NewSessionForm(forms.ModelForm):
    class Meta:
        model = sessao
        fields = ["Dia", "Inicio","Duraçao","Vagas", "Espaço","Materiais","Colaboradores"]
        widgets = {
            'Dia': forms.Select(attrs={'class': 'form-control' ,'required': True}),
            'Inicio': forms.Select(attrs={'class': 'form-control', 'type': 'time'}),
            'Vagas': forms.TextInput(attrs={'class': 'form-control'}),
            'Espaço': forms.TextInput(attrs={'class': 'form-control'}),
            'Materiais': forms.Textarea(attrs={'class': 'form-control'}),
            'Colaboradores': forms.NumberInput(attrs={'min':0,'class': 'form-control'}),
        }