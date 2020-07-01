from django.shortcuts import render, redirect, get_object_or_404
from .models import tarefa, disponibilidade
from utilizador.models import utilizador
from .filters import TarefaFilter, DisponibilidadeFilter
from .forms import DisponibilidadeForm
from datetime import datetime, date, timedelta
from configuracoes.models import main, dias_DA
from django.contrib.messages.views import SuccessMessageMixin

def tarefas_atribuidas(request):
  if request.user.is_authenticated:
    if request.user.TipoUtilizador == "Colaborador":
      try:
          #tarefas = tarefa.objects.filter(UtilizadorID2=request.user.id)
          user_filter = TarefaFilter(request.GET, queryset=tarefa.objects.filter(UtilizadorID2=request.user.id))
      except tarefa.DoesNotExist:
          tarefas = None
      return render(request=request,
                    template_name='tarefas/tarefas_atribuidas.html',
                    context={"filter": user_filter})
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")

def concluir_tarefa(request, pk):
  if request.user.is_authenticated:
    tar = get_object_or_404(tarefa, pk=pk)
    if tar.UtilizadorID2.id.id == request.user.id:
      tar.Concluida = 1
      tar.save()
      messages.success(request, "Tarefa concluída com sucesso")
      return redirect("tarefas:tarefas_atribuidas")
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")


def disponibilidades(request):
  if request.user.is_authenticated:
    if request.user.TipoUtilizador == "Colaborador":
      try:
        #disp = disponibilidade.objects.filter(UtilizadorID = request.user.id)
        user_filter = DisponibilidadeFilter(request.GET, queryset=disponibilidade.objects.filter(UtilizadorID = request.user.id))
      except disponibilidade.DoesNotExist:
        disp = None
      return render(request=request,
                      template_name='tarefas/disponibilidades.html',
                      context={"filter": user_filter})
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")

def create_disponibilidade(request):
  if request.user.is_authenticated:
    if request.user.TipoUtilizador == "Colaborador":
      context ={}
      tipo = "Adicionar"
      # create object of form
      form = DisponibilidadeForm(request.POST or None, request.FILES or None)

      # check if form data is valid
      if form.is_valid():
          article = form.save(commit=False)
          article.UtilizadorID = utilizador.objects.get(id = request.user.id)
          article.save()
          messages.success(request, "Disponibilidade adicioniada com sucesso")
          return redirect("tarefas:disponibilidades")

      context['form']= form
      context['tipo']= tipo
      return render(request, "tarefas/create_disponibilidades.html", context)
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")

def edit_disponibilidade(request, pk):
  if request.user.is_authenticated:
    disp = get_object_or_404(disponibilidade, pk=pk)
    if disp.UtilizadorID.id == request.user.id:
      form = DisponibilidadeForm(request.POST or None, instance=disp)
      tipo = "Editar"
      if request.method == 'POST':
          if form.is_valid():
              form.save()
              messages.success(request, "Disponibilidade alterada com sucesso")
              return redirect("tarefas:disponibilidades")
      context = {
          'form': form,
          'disp': disp,
          'tipo': tipo
      }
      return render(request, "tarefas/create_disponibilidades.html", context)
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")

def delete_disponibilidade(request, pk):
  if request.user.is_authenticated:
    disp = get_object_or_404(disponibilidade, pk=pk)
    if disp.UtilizadorID.id == request.user.id:
      disp.delete()
      messages.success(request, "Disponibilidade eliminada com sucesso")
      return redirect("tarefas:disponibilidades")
    else:
      return redirect("inicial:inicial")
  else:
      return redirect("utilizador:login")

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import tarefa, actividade, disponibilidade
from utilizador.models import colab, coord
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewtarefaForm
from django.views.generic import TemplateView, ListView, UpdateView
from django.urls import reverse
from .filters import TarefaFilter, ColabFilter
from django.forms.widgets import RadioSelect
# Create your views here.
from utilizador.forms import NewUtilizadorForm
from configuracoes.models import uos
from django.contrib.messages.views import SuccessMessageMixin

def deletetarefaAction(request, delete,*args, **kwargs):
     if request.user.TipoUtilizador == "Coordenador":
         this_user = tarefa.objects.get(id=delete)
         if this_user.UtilizadorID2:
             colabs = colab.objects.get(username=this_user.UtilizadorID2)
             colabs.atribuido = '0'
             colabs.save()
         this_user.delete()
         messages.success(request, "Tarefa eliminada com sucesso")
         return redirect("tarefas:homepage")
     else:
         return render(request=request,
                       template_name="tarefas/erro.html")

def createtarefa(request,*args, **kwargs):
    if request.user.TipoUtilizador == "Coordenador":
        form = NewtarefaForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            form = NewtarefaForm(request.POST)
            print(form.instance.Dia)
            if form.is_valid():
                # print(form)
                form.save(commit=False);
                form.instance.UtilizadorID = coord.objects.get(id=request.user.id)
                form.save()
                messages.success(request, "Tarefa criada com sucesso")
                return redirect("tarefas:homepage")
        return render(request=request,
                      template_name="tarefas/edit_Tarefa.html",
                      context={"form":form, "actall":actividade.objects.filter(EntidadeOrganizacional=request.user.UO), 'dia':dias_DA.objects.all()})
    else:
        return render(request=request,
                      template_name="tarefas/erro.html")

class TarefaUpdateView(UpdateView, SuccessMessageMixin):
        success_message='Tarefa alterada com sucesso'
        model = tarefa
        fields = ["Nome","Dia","HorasInicio","HorasFim","Tipo","Origem","Destino","Grupos","Descricao","Nome_actividade"]
        template_name = "tarefas/edit_Tarefa.html"
        def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(TarefaUpdateView,self).post(request,**kwargs)
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['dia'] = dias_DA.objects.all()
            if self.object.Nome_actividade != None:
                context['act1']= actividade.objects.get(id=self.object.Nome_actividade.id)
                context['actall']= actividade.objects.all()
            return context

        def get_success_url(self, **kwargs):
            return reverse("tarefas:homepage")

def TarefaView(request, id):
    if request.user.TipoUtilizador == "Coordenador":
        return render(request=request,
                  template_name="tarefas/detail_tarefa.html",
                  context={"coord": coord.objects.get(id=request.user.id),"utilizador":tarefa.objects.get(id=id)})
    elif request.user.TipoUtilizador == "Administrador":
        return render(request=request,
                  template_name="tarefas/detail_tarefa.html",
                  context={"utilizador":tarefa.objects.get(id=id)})
    else:
        uti = colab.objects.get(id=request.user.id)
        return render(request=request,
                  template_name="tarefas/detail_tarefa.html",
                  context={"utilizador":tarefa.objects.get(UtilizadorID2=uti, id=id)})

class AtribuirColabUpdateView(TemplateView):
    success_message='Colaborador atribuido com sucesso'
    template_name = 'tarefas/atribuir_colab.html'
    def get_success_url(self, **kwargs):
        return reverse("tarefas:homepage")

    def get(self, request, pk, *args,**kwargs):
        if request.user.TipoUtilizador == "Coordenador":
            context = super(AtribuirColabUpdateView, self).get_context_data(**kwargs)
            uti = coord.objects.get(id=request.user.id).UO
            uti = colab.objects.filter(UO=uti)

            tar = tarefa.objects.get(id=pk)
            disps = disponibilidade.objects.filter(Dia=tar.Dia, Inicio__lte=tar.HorasInicio, Fim__gte=tar.HorasFim)

            context["atribuido"] = tarefa.objects.get(id=pk).UtilizadorID2
            context["filter"] = ColabFilter(request.GET, queryset=uti)
            context["disps"] = disps
            return self.render_to_response(context)
        else:
            return render(request=request,
                          template_name="tarefas/erro.html")
    def post(self, request, pk, *args,**kwargs):
        print(request.POST['username'])
        swag = tarefa.objects.get(id=pk)
        swag.UtilizadorID2 = colab.objects.get(username=request.POST["username"])
        swag.save()
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(reverse("tarefas:homepage"))

def RetirarColab(request, delete, pk,*args, **kwargs):
     if request.user.TipoUtilizador == "Coordenador":
         this_user = tarefa.objects.get(id=pk)
         this_user.UtilizadorID2 = None
         this_user.save()
         messages.success(request, "Colaborador retirado com sucesso")
         return redirect("tarefas:homepage")
     else:
         return render(request=request,
                       template_name='tarefas/erro.html')


def colaboradores(request):
    if request.user.TipoUtilizador == "Coordenador":
        uti = coord.objects.get(id=request.user.id).UO
    elif request.user.TipoUtilizador == "Colaborador":
        uti = colab.objects.get(id=request.user.id).UO
    else:
        return render(request=request,
                      template_name='tarefas/erro.html')
    user_filter = ColabFilter(request.GET, queryset=colab.objects.filter(UO=uti))
    return render(request=request,
                  template_name='tarefas/colaboradores.html',
                  context={"isco":request.user.TipoUtilizador, "disponibilidade": disponibilidade.objects.all(),"filter": user_filter,"tarefa": tarefa.objects.all})

def homepage(request):
    if request.user.TipoUtilizador == "Coordenador":
        uti = coord.objects.get(id=request.user.id)
        tarefa_filter = TarefaFilter(request.GET, queryset=tarefa.objects.filter(UtilizadorID=uti))
        return render(request=request,
                      template_name='tarefas/tarefas.html',
                      context={"filter": tarefa_filter, "tarefa": tarefa.objects.all})
    elif request.user.TipoUtilizador == "Administrador":
        tarefa_filter = TarefaFilter(request.GET, queryset=tarefa.objects.all())
        return render(request=request,
                      template_name='tarefas/tarefas.html',
                      context={"filter": tarefa_filter, "tarefa": tarefa.objects.all})
    else:
        return render(request=request,
                      template_name='tarefas/erro.html')


def register(request):
    if request.POST:
        form = NewUtilizadorForm(request.POST)
        if form.is_valid():
            form.save()

            if request.POST.get('TipoUtilizador') == 'Coordenador':
                UO = uos.objects.get(id=request.POST.get('UO')).sigla
                p = coord(id=utilizador.objects.get(username=request.POST.get('username')),username=request.POST.get('username'),UO=UO)
                p.save()
            elif request.POST.get('TipoUtilizador') == 'Colaborador':
                UO = uos.objects.get(id=request.POST.get('UO')).sigla
                p = colab(id=utilizador.objects.get(username=request.POST.get('username')),username=request.POST.get('username'),UO=UO)
                p.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect("tarefas:colaboradores")

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
