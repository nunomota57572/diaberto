from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import utilizador, colab, coord
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import NewUtilizadorForm, AccountUpdateForm
from django.views.generic import UpdateView
from django.urls import reverse
from .filters import UtilizadorFilter
from django.contrib.auth.decorators import login_required
from configuracoes.models import uos
from inscricoes.models import inscricao1
from notificacao.models import Notificacao
from notificacao.forms import AutoNotif
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def detail_utilizador(request, id):
    inscricao = ''
    if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
        inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
    if request.user.is_authenticated:
        this_user = utilizador.objects.get(id=id)
        return render(request=request, template_name='main/detail_utilizador.html', context={"utilizador": this_user, "inscricao":inscricao})
    else:
        return redirect("inicial:inicial")

def show_utilizadores(request):
    if request.user.is_authenticated:
        if request.user.TipoUtilizador == "Coordenador" or request.user.TipoUtilizador == "Administrador":
            utilizador_filter = UtilizadorFilter(request.GET, queryset=utilizador.objects.all())
            if utilizador_filter:
                return render(request=request,
                    template_name='main/utilizadores.html',
                    context={"utilizadores": utilizador_filter})
            else:
                return redirect("utilizador:util")
        else:
            return redirect("inicial:inicial")
    else:
        return redirect("utilizador:login")

def register(request):
    if request.POST:
        form = NewUtilizadorForm(request.POST)
        notif = AutoNotif(request.POST)
        if form.is_valid():
            form.save()
            
            if request.POST.get('TipoUtilizador') == 'Coordenador':
                UO = uos.objects.get(id=request.POST.get('UO')).sigla
                p = coord(id=utilizador.objects.get(username=request.POST.get('username')),username=request.POST.get('username'),UO=UO)
                p.save()
                messages.success(request, "Coordenador registado com sucesso")
            elif request.POST.get('TipoUtilizador') == 'Colaborador':
                UO = uos.objects.get(id=request.POST.get('UO')).sigla
                p = colab(id=utilizador.objects.get(username=request.POST.get('username')),username=request.POST.get('username'),UO=UO)
                p.save()
                messages.success(request, "Colaborador registado com sucesso")
            elif request.POST.get('TipoUtilizador') == 'Administrador':
                messages.success(request, "Administrador registado com sucesso")
            elif request.POST.get('TipoUtilizador') == 'Participante':
                messages.success(request, "Participante registado com sucesso")
            else:
                messages.success(request, "Professor Universitário registado com sucesso")

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            notif.instance.autorid=utilizador.objects.get(id=1)
            notif.instance.is_read=0
            notif.instance.assunto="Bem-Vindo"
            notif.instance.descricao="Bem-Vindo, ao website do dia aberto da UALG, a partir do momento que a sua conta for validada por um administrador poderá realizar a sua inscrição. Obrigado, admin."
            notif.instance.remetenteid=utilizador.objects.get(username=username)
            notif.save()  
            login(request, user)
            
            return redirect("inicial:inicial")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = NewUtilizadorForm()
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Até à próxima")
    return redirect("inicial:inicial")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Bem vindo, {username}")
                return redirect("inicial:inicial")
            else:
                messages.error(request, "Username or Palavra-passe inválido.")
        else:
            messages.error(request, "Username or Palavra-passe inválido.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})

class editar(UpdateView):
        success_message='Utilizador alterado com sucesso'
        model = utilizador
        form_class = AccountUpdateForm
        template_name = 'main/conta.html'
        def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(editar,self).post(request,**kwargs)
        def get_success_url(self,**kwargs):
            return reverse("inicial:inicial")  

def delete(request, id):
    if request.user.is_authenticated:
        if request.user.TipoUtilizador == "Administrador" or request.user.TipoUtilizador == "Coordenador":
            obj = utilizador.objects.get(id=id)
            obj.delete()
            messages.success(request, obj.username + " eliminado com sucesso")
            return redirect('utilizador:util')
        else:
            return redirect("inicial:inicial")
    else:
        return redirect("utilizador:login")

def validar_utilizador(request, pk):
    if request.user.is_authenticated:
        if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
            tar = get_object_or_404(utilizador, pk=pk)
            tar.Estado = 1
            tar.save()
            messages.success(request, tar.username + " validado com sucesso")
            return redirect("utilizador:util")
        else:
            return redirect("inicial:inicial")
    else:
        return redirect("utilizador:login")