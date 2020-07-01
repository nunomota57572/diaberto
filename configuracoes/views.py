from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from datetime import datetime, date, timedelta
import datetime
from django.views.generic import UpdateView
from django.urls import reverse
from .models import main, horarios_transportes, horarios_atividades, escolas, departamentos, cursos, uos, dias_DA, horas_transportes, horas_atividades
from .forms import NewGeralForm, NewHorarioTransporteForm, NewHorarioAtividadeForm, NewEscolaForm, NewDepartamentoForm, NewCursoForm, NewUOForm
from .filters import FilterEscolas, FilterUO, FilterDepartamento, FilterCurso
import json
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def geral(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			year = date.today().year
			# year = 1123

			this_ano_val = main.objects.filter(ano=year)
			if this_ano_val:
				today = datetime.date.today()
				this_ano = main.objects.get(ano=year)

				if this_ano.dataDiaAbertoInicio <= today and this_ano.dataDiaAbertoFim >= today:
					return render(request=request, template_name='configuracoes/geral.html', context={"text": "Site do Dia Aberto disponível", "da": this_ano})
				else:
					return render(request=request, template_name='configuracoes/geral.html', context={"text": "Site do Dia Aberto indisponível", "da": this_ano})
			else:
				return render(request=request, context={"text": "Ano não registado!"}, template_name='configuracoes/geral.html')
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def new_geral(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			if request.method == 'POST':
				form = NewGeralForm(request.POST)
				if form.is_valid():
					form.save()

					dia_i = form.instance.dataDiaAbertoInicio
					dia_f = form.instance.dataDiaAbertoFim
					delta = dia_f - dia_i
					dias_DA.objects.all().delete()
					for i in range(delta.days + 1):
						d = dia_i + timedelta(days=i)
						p = dias_DA(data=d)
						p.save()
					messages.success(request, "Configurações gerais adicionadas com sucesso")

				else:
					return render(request=request, template_name='configuracoes/new_geral.html', context={"form":form})

				return redirect("configuracoes:geral")
			else:
				form = NewGeralForm()
			return render(request=request, template_name='configuracoes/new_geral.html', context={"form":form})
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_geral(UpdateView):
	success_message='Configurações gerais alteradas com sucesso'
	model = main
	form_class = NewGeralForm
	template_name = 'configuracoes/edit_geral.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_geral,self).post(request,**kwargs)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['act1']= main.objects.get(ano=2020)
		return context

	def get_success_url(self, **kwargs):
		return reverse("configuracoes:geral")

def delete_geral(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			main1 = main.objects.get(id=id)
			main1.delete()
			messages.success(request, "Configurações gerais eliminadas com sucesso")
			return redirect("configuracoes:geral")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def horario_transporte(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			h = horarios_transportes.objects.all()
			if request.method == 'POST':
				form = NewHorarioTransporteForm(request.POST)
				if form.is_valid():
					horarios_transportes.objects.all().delete()
					horas_transportes.objects.all().delete()

					inicio = form.instance.inicio
					fim = form.instance.fim
					periodo = form.instance.periodo
					ini = inicio * 60
					f = fim * 60
					duracao = (f - ini) // periodo + 1
					for i in range(duracao):
						h = ini // 60
						m = ini % 60 
						hm = str("%02d" % h) + ":" + str("%02d" % m)
						tempo = horas_transportes(tempo=hm)
						tempo.save()
						ini = ini + periodo
					form.save()
					messages.success(request, "Horário tranportes adicionado com sucesso")
				else:
					return render(request,"configuracoes/horario_transporte.html",{'horario':h, "form":form})

				return redirect("configuracoes:horario_transporte")
			else:
				form = NewHorarioTransporteForm()

			return render(request,"configuracoes/horario_transporte.html",{'horario':h, "form":form}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def delete_horario_transporte(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			h = horarios_transportes.objects.all()
			h.delete()
			messages.success(request, "Horário tranportes eliminado com sucesso")
			return redirect("configuracoes:horario_transporte")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def horario_atividade(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			h = horarios_atividades.objects.all()
			if request.method == 'POST':
				form = NewHorarioAtividadeForm(request.POST)
				if form.is_valid():
					horarios_atividades.objects.all().delete()
					horas_atividades.objects.all().delete()

					inicio = form.instance.inicio
					fim = form.instance.fim
					periodo = form.instance.periodo
					ini = inicio * 60
					f = fim * 60
					duracao = (f - ini) // periodo + 1
					for i in range(duracao):
						h = ini // 60
						m = ini % 60 
						hm = str("%02d" % h) + ":" + str("%02d" % m)
						tempo = horas_atividades(tempo=hm)
						tempo.save()
						ini = ini + periodo
					form.save()
					messages.success(request, "Horário atividades adicionado com sucesso")
				else:
					return render(request,"configuracoes/horario_atividade.html",{'horario':h, "form":form})

				return redirect("configuracoes:horario_atividade")
			else:
				form = NewHorarioAtividadeForm()

			return render(request,"configuracoes/horario_atividade.html",{'horario':h, "form":form})
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def delete_horario_atividade(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			h = horarios_atividades.objects.all()
			h.delete()
			messages.success(request, "Horário atividades eliminado com sucesso")
			return redirect("configuracoes:horario_atividade")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def escola(request):  
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			escola = escolas.objects.all()

			myFilter = FilterEscolas(request.GET, queryset=escola)
			escola = myFilter.qs

			if request.method == 'POST':
				form = NewEscolaForm(request.POST)
				if form.is_valid():
					form.save()
					messages.success(request, "Escola adicionada com sucesso")
				else:
					return render(request,"configuracoes/escola.html",{'escola':escola, "form":form, 'myFilter':myFilter}) 
				return redirect("configuracoes:escola")
			else:
				form = NewEscolaForm()  
			return render(request,"configuracoes/escola.html",{'escola':escola, "form":form, 'myFilter':myFilter}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_escola(UpdateView):
	success_message='Escola alterada com sucesso'
	model = escolas
	form_class = NewEscolaForm
	template_name = 'configuracoes/edit_escola.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_escola,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("configuracoes:escola")

def delete_escola(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			escola = escolas.objects.get(id=id)
			# if request.method == "POST"
			escola.delete()
			messages.success(request, "Escola eliminada com sucesso")
			return redirect("configuracoes:escola")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def uo(request):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:  
			uo = uos.objects.all()  

			myFilter = FilterUO(request.GET, queryset=uo)
			uo = myFilter.qs

			if request.method == 'POST':
				form = NewUOForm(request.POST)
				if form.is_valid():
					form.save()
					messages.success(request, "Unidade orgânica adicionada com sucesso")
				else:
					return render(request,"configuracoes/uo.html",{'uo':uo, "form":form,'myFilter':myFilter}) 
				return redirect("configuracoes:uo")
			else:
				form = NewUOForm()
			return render(request,"configuracoes/uo.html",{'uo':uo, "form":form,'myFilter':myFilter}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_uo(UpdateView):
	success_message='Unidade orgânica alterada com sucesso'
	model = uos
	form_class = NewUOForm
	template_name = 'configuracoes/edit_uo.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_uo,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("configuracoes:uo")

def delete_uo(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			uo = uos.objects.get(id=id)
			uo.delete()
			messages.success(request, "Unidade orgânica eliminada com sucesso")
			return redirect("configuracoes:uo")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def departamento(request):  
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			departamento = departamentos.objects.all()

			myFilter = FilterDepartamento(request.GET, queryset=departamento)
			departamento = myFilter.qs

			if request.method == 'POST':
				form = NewDepartamentoForm(request.POST)
				if form.is_valid():
					form.save()
					messages.success(request, "Departamento adicioniado com sucesso")
				else:
					return render(request,"configuracoes/departamento.html",{'departamento':departamento, "form":form,'myFilter':myFilter}) 
				return redirect("configuracoes:departamento")
			else:
				form = NewDepartamentoForm()  
			return render(request,"configuracoes/departamento.html",{'departamento':departamento, "form":form,'myFilter':myFilter}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_departamento(UpdateView):
	success_message='Departamento alterado com sucesso'
	model = departamentos
	form_class = NewDepartamentoForm
	template_name = 'configuracoes/edit_departamento.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_departamento,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("configuracoes:departamento")

def delete_departamento(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			departamento = departamentos.objects.get(id=id)
			departamento.delete()
			messages.success(request, "Departamento eliminado com sucesso")
			return redirect("configuracoes:departamento")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def curso(request):  
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			curso = cursos.objects.all()  

			myFilter = FilterCurso(request.GET, queryset=curso)
			curso = myFilter.qs

			if request.method == 'POST':
				form = NewCursoForm(request.POST)
				if form.is_valid():
					form.save()
					messages.success(request, "Curso adicioniado com sucesso")
				else:
					return render(request,"configuracoes/curso.html",{'curso':curso, "form":form, 'myFilter':myFilter}) 
				return redirect("configuracoes:curso")
			else:
				form = NewCursoForm()

			return render(request,"configuracoes/curso.html",{'curso':curso, "form":form, 'myFilter':myFilter}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_curso(UpdateView):
	success_message='Curso alterado com sucesso'
	model = cursos
	form_class = NewCursoForm
	template_name = 'configuracoes/edit_curso.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_curso,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("configuracoes:curso")

def delete_curso(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			curso = cursos.objects.get(id=id)
			curso.delete()
			messages.success(request, "Curso eliminado com sucesso")
			return redirect("configuracoes:curso")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")
