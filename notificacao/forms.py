from django import forms
from notificacao.models import Notificacao


class NewNotificacao(forms.ModelForm):
    class Meta:
        model = Notificacao
        fields = ["assunto","descricao","remetenteid"]   
        widgets = {
            'assunto': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'remetenteid': forms.Select(attrs={'class': 'form-control'}),
        }

class AutoNotif(forms.ModelForm):
    class Meta:
        model=Notificacao
        fields = []





