from django import forms
from django.contrib.auth.forms import UserCreationForm
from utilizador.models import utilizador
from configuracoes.models import uos, departamentos, cursos


class NewUtilizadorForm(UserCreationForm):
    #email = forms.EmailField(max_length=60)
    
    class Meta:
        model = utilizador
        fields = ("Nome", "username", "email", "password1",
                  "password2", "Telefone", "TipoUtilizador", "UO", "Departamento", "Curso")
        widgets = {
			'Nome': forms.TextInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
			'Telefone': forms.TextInput(attrs={'class': 'form-control'}),
			'TipoUtilizador': forms.Select(attrs={'class': 'form-control'}),
			'UO': forms.Select(attrs={'class': 'form-control'}),
			'Departamento': forms.Select(attrs={'class': 'form-control'}),
			'Curso': forms.Select(attrs={'class': 'form-control'}),
		}
    def save(self, commit=True):
        user = super(NewUtilizadorForm, self).save(commit=False)
        #user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = utilizador
        fields = ("Nome", "username", "email","Telefone")
        widgets = {
			'Nome': forms.TextInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'Telefone': forms.TextInput(attrs={'class': 'form-control'}),
		}

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = utilizador.objects.exclude(
                pk=self.instance.pk).get(email=email)
        except utilizador.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = utilizador.objects.exclude(
                pk=self.instance.pk).get(username=username)
        except utilizador.DoesNotExist:
            return username
        raise forms.ValidationError(
            'Username "%s" is already in use.' % username)

    def clean_Nome(self):
        Nome = self.cleaned_data['Nome']
        return Nome

    def clean_Telefone(self):
        Telefone = self.cleaned_data['Telefone']
        return Telefone

    
