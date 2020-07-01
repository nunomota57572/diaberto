from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import atividade, sessao
from django.contrib import messages
from .forms import NewAtividadeForm, NewSessionForm
from .forms import forms
from django.views.generic import UpdateView
from django.urls import reverse
from utilizador.models import utilizador
from .filters import AtividadeFilter
from configuracoes.models import uos, departamentos
from notificacao.models import Notificacao
from notificacao.forms import AutoNotif
from inscricoes.models import inscricao_atividades, inscricao1
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def AtividadeView(request, id):

    this_atividade = atividade.objects.get(id=id)
    this_session = sessao.objects.get(Atividade__id=id)

    return render(request=request,
                  template_name='main/atividade.html',
                  context={"atividade": this_atividade, "sessao": this_session})


def deleteatividadeAction(request, delete):
    if request.user.TipoUtilizador == "Professor Universitario":
        this_user = atividade.objects.get(id=delete)
        this_user.delete()
        messages.success(request, "Atividade eliminada com sucesso")
        return redirect("atividades:homepage")
    else:
        return redirect("inicial:inicial")



def createActividade(request):

    if request.user.TipoUtilizador == "Professor Universitario":
        if request.method == 'POST':
            form = NewAtividadeForm(request.POST)
            sessao = NewSessionForm(request.POST)

            if form.is_valid() and sessao.is_valid():
                form.save(commit=False)
                sessao.save(commit=False)
                form.instance.EntidadeOrganizacional = uos.objects.get(sigla = request.user.UO)
                form.instance.Departamento = departamentos.objects.get(departamento = request.user.Departamento)
                form.instance.Criador = utilizador.objects.get(id=request.user.id)
                form.save()
                sessao.instance.Atividade = atividade.objects.get(id=form.instance.id)
                sessao.save()
                messages.success(request, "Atividade criada com sucesso")
                return redirect("atividades:homepage")
        else:
            form = NewAtividadeForm()
            sessao = NewSessionForm()
        return render(request=request,
                    template_name='main/createActividade.html',
                    context={"form": form, "sessao": sessao})
    else:
        return redirect("inicial:inicial")


class AtividadeUpdateView(UpdateView):
    success_message='Atividade alterada com sucesso'
    model = atividade
    form_class = NewAtividadeForm
    template_name = "main/createActividade.html"

    def get_context_data(self, **kwargs):
        context = super(AtividadeUpdateView, self).get_context_data(**kwargs)
        context['sessao'] = NewSessionForm(
            instance=sessao.objects.get(Atividade__id=self.kwargs['pk']))
        return context

    def post(self, request, *args, **kwargs):
        sform = NewSessionForm(data=self.request.POST, instance=sessao.objects.get(Atividade__id=self.kwargs['pk']))
        sform.save()
        messages.success(self.request, self.success_message)
        Participantes = []
        Participantes = utilizador.objects.filter(TipoUtilizador="Participante").values_list('id', flat=True)
        for x in Participantes:
                if inscricao_atividades.objects.filter(inscricaoID__UtilizadorID=x,sessao__Atividade=self.kwargs['pk']).count()>0:
                    notif = AutoNotif(request.POST)
                    notif.instance.autorid=utilizador.objects.get(id=1)
                    notif.instance.is_read=0
                    notif.instance.assunto="Alterações na atividade"
                    notif.instance.descricao="A atividade {} em que está inscrito sofreu alterações.".format(atividade.objects.get(id=self.kwargs['pk']).Nome_actividade)
                    notif.instance.remetenteid=utilizador.objects.get(id=x)
                    notif.save()

        return super(AtividadeUpdateView, self).post(request, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse("atividades:homepage")


def homepage(request):
    if request.user.username:
        if request.user.TipoUtilizador == "Professor Universitario":
            atividade_filter = AtividadeFilter(request.GET, queryset=atividade.objects.filter(Criador = request.user.id))
            return render(request=request,
                    template_name='main/home.html',
                    context={"atividades": atividade_filter})
        elif request.user.TipoUtilizador == "Coordenador":
            atividade_filter = AtividadeFilter(request.GET, queryset=atividade.objects.filter(EntidadeOrganizacional = uos.objects.get(sigla = request.user.UO)))
            return render(request=request,
                    template_name='main/home.html',
                    context={"atividades": atividade_filter})
        elif request.user.TipoUtilizador == "Administrador":
            atividade_filter = AtividadeFilter(request.GET, queryset=atividade.objects.all())
            return render(request=request,
                    template_name='main/home.html',
                    context={"atividades": atividade_filter})


def validar_Atividade(request, pk):
    if request.user.is_authenticated:
        if request.user.TipoUtilizador == "Coordenador":
            tar = get_object_or_404(atividade, pk=pk)
            tar.Estado = 'Aceite'
            tar.save()
            messages.success(request, "Atividade Aceite com sucesso")
            return redirect("atividades:homepage")
        else:
            return redirect("inicial:inicial")
    else:
        return redirect("utilizador:login")


def rejeitar_Atividade(request, pk):
    if request.user.is_authenticated:
        if request.user.TipoUtilizador == "Coordenador":
            tar = get_object_or_404(atividade, pk=pk)
            tar.Estado = 'Rejeitada'
            tar.save()
            messages.success(request, "Atividade Rejeitada com sucesso")
            return redirect("atividades:homepage")
        else:
            return redirect("inicial:inicial")
    else:
        return redirect("utilizador:login")
