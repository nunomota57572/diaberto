from django import forms
from datetime import datetime, date, timedelta
from django.contrib.auth.forms import UserCreationForm
from .models import disponibilidade, coord, colab
from configuracoes.models import main
from utilizador.forms import NewUtilizadorForm

class DisponibilidadeForm(forms.ModelForm):

    #Dia = forms.DateField(required = True, widget=forms.Select(choices=days()))

    class Meta:
        model = disponibilidade
        exclude = ['Id', 'UtilizadorID']
        widgets = {
            'Dia': forms.Select(attrs={'class': 'form-control' ,'required': True}),
            'Inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'Fim': forms.TimeInput(attrs={'class': 'form-control','type': 'time'}),
            'Observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }

    def clean(self):
        cleaned_data = super(DisponibilidadeForm, self).clean()
        Dia = self.cleaned_data.get('Dia')
        Inicio = self.cleaned_data.get('Inicio')
        Fim = self.cleaned_data.get('Fim')
        Observacoes = self.cleaned_data.get('Observacoes')
        if Inicio >= Fim:
            raise forms.ValidationError('A hora final não pode ser maior ou igual a hora inicial.')


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import tarefa
from utilizador.models import colab, coord

TITLE_CHOICES = [
    ('Atividade', 'Atividade'),
    ('Acompanhar participantes', 'Acompanhar participante'),
    ('Outro', 'Outro'),
]

class NewtarefaForm(forms.ModelForm):
    class Meta:
        model = tarefa
        fields = ["Dia","Nome","HorasInicio","HorasFim","Tipo","Origem","Destino","Grupos","Descricao","Nome_actividade"]

    def clean(self):
        cleaned_data = super(NewtarefaForm, self).clean()
        Nome = self.cleaned_data.get('Nome')
        Dia = self.cleaned_data.get('Dia')
        Tipo = self.cleaned_data.get('Tipo')
        Origem = self.cleaned_data.get('Origem')
        Destino = self.cleaned_data.get('Destino')
        Grupos = self.cleaned_data.get('Grupos')
        Descricao = self.cleaned_data.get('Descricao')
        Nome_actividade = self.cleaned_data.get('Nome_actividade')
        HorasInicio = self.cleaned_data.get('HorasInicio')
        HorasFim = self.cleaned_data.get('HorasFim')
        if HorasInicio >= HorasFim:
            raise forms.ValidationError('A hora final não pode ser menor ou igual a hora inicial.')


class ColabForm(forms.ModelForm):
    class Meta:
        model = colab
        fields = ["username"]

class CoordForm(forms.ModelForm):
    class Meta:
        model = coord
        fields = ["username"]
