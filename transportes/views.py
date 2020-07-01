from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import autocarros, percursos
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from datetime import date, timedelta
import datetime 
from .forms import NewAutocarroForm, NewPercursoForm, NewEditPercursoForm
from django.views.generic import UpdateView
from django.urls import reverse
from .filters import FilterAutocarro, FilterPercurso
from configuracoes.models import main, escolas
from inscricoes.models import inscricoes, atividades_inscritas
from atividades.models import atividades, sessoes
from django.contrib.messages.views import SuccessMessageMixin
from inscricoes.models import inscricao1

def autocarro(request): 
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True: 
			
			autocarro = autocarros.objects.all() 
			if request.method == 'POST':
				form = NewAutocarroForm(request.POST)
				if form.is_valid():
					form.save()
					messages.success(request, "Autocarro adicioniado com sucesso")
				else:
					return render(request,"transportes/autocarro.html",{'autocarro':autocarro, "form":form})
				return redirect("transportes:autocarro") 
			else:
				form = NewAutocarroForm()
		
			return render(request,"transportes/autocarro.html",{'autocarro':autocarro, "form":form}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")
		
def percurso_autocarro(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			autocarro = autocarros.objects.get(id=id)
			percurso_from_id = percursos.objects.filter(identificador=id)

			myFilter = FilterPercurso(request.GET, queryset=percurso_from_id)
			percurso_from_id = myFilter.qs

			if request.method == 'POST':
				form = NewPercursoForm(data=request.POST, autocarro=autocarro)
				if form.is_valid():
					form.save(commit=False)
					form.instance.identificador = autocarro
					form.instance.lotacao = '0'
					form.instance.lugares_restantes = autocarro.capacidade
					form.save()
					messages.success(request, "Percurso adicioniado com sucesso")
				else:
					return render(request,"transportes/new_percurso.html",{'autocarro': autocarro, 'percurso':percurso_from_id, 'form':form, 'myFilter':myFilter})

				return redirect("transportes:percurso_autocarro", id)
			else:
				form = NewPercursoForm()
			return render(request,"transportes/new_percurso.html",{'autocarro': autocarro, 'percurso':percurso_from_id, 'form':form, 'myFilter':myFilter}) 
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

class edit_autocarro(UpdateView):
	success_message='Autocarro alterado com sucesso'
	model = autocarros
	form_class = NewAutocarroForm
	template_name = 'transportes/edit_autocarro.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_autocarro,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("transportes:autocarro")	

def delete_autocarro(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			autocarro = autocarros.objects.get(id=id)
			autocarro.delete()
			messages.success(request, "Autocarro eliminado com sucesso")
			return redirect("transportes:autocarro")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")

def percurso(request): 
	 
	autocarro = autocarros.objects.all()
	percurso = percursos.objects.all()  

	myFilter = FilterPercurso(request.GET, queryset=percurso)
	percurso = myFilter.qs

	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)

	return render(request,"transportes/percurso.html",{'percurso':percurso, 'autocarro':autocarro, 'myFilter':myFilter,  "inscricao":inscricao}) 

def atribuir_a_percurso(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			percurso_from_id = percursos.objects.get(id=id)
			autocarro = autocarros.objects.get(id=percurso_from_id.identificador_id)
			#atividade = atividades.objects.filter(campus=percurso_from_id.destino)
			atividade = atividades.objects.all()
			atividade_inscrita = atividades_inscritas.objects.all()
			sessao = sessoes.objects.all()
			inscricao = inscricoes.objects.filter(necessitaTransporte=True, horaInicio__lte=percurso_from_id.horario, nParticipantes__lte=percurso_from_id.lugares_restantes)

			if request.method == 'POST':
				form = NewPercursoForm(data=request.POST, autocarro=autocarro)
				if form.is_valid():
					form.save(commit=False)
					form.instance.identificador = autocarro
					form.instance.lotacao = '0'
					form.save()
				else:
					return render(request,"transportes/atribuir.html",{'percurso':percurso_from_id, 
						'autocarro':autocarro,
						'inscricao':inscricao, 
						'atividade_inscrita':atividade_inscrita, 
						'atividade':atividade,
						'sessao': sessao})

				return redirect("transportes:atribuir_a_percurso", id)
			else:
				form = NewPercursoForm()

			return render(request,"transportes/atribuir.html",{'percurso':percurso_from_id, 
						'autocarro':autocarro,
						'inscricao':inscricao, 
						'atividade_inscrita':atividade_inscrita, 
						'atividade':atividade,
						'sessao': sessao})
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")	

class edit_percurso(UpdateView):
	success_message='Percurso alterado com sucesso'
	model = percursos
	form_class = NewEditPercursoForm
	template_name = 'transportes/edit_percurso.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_percurso,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("transportes:percurso")	

def delete_percurso(request, id):
	if request.user.is_authenticated:
		if request.user.TipoUtilizador == "Administrador" and request.user.Estado == True:
			percurso = percursos.objects.get(id=id)
			percurso.delete()
			messages.success(request, "Percurso eliminado com sucesso")
			return redirect("transportes:percurso")
		else:
			return redirect("inicial:inicial")
	else:
		return redirect("utilizador:login")