from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import menus, ementas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from datetime import date
import datetime 
from .forms import NewMenuForm, NewEmentaForm
from django.views.generic import UpdateView
from django.urls import reverse
from .filters import FilterEmentas
from inscricoes.models import inscricao1
from .models import menus

def menu(request):
	menu = menus.objects.all() 
	if request.method == 'POST':
		form = NewMenuForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Menu adicioniado com sucesso")
		else:
			return render(request=request, template_name='almocos/menu.html', context={"form":form, "menu":menu})
		return redirect("almocos:menu")
	else:
		form = NewMenuForm()
	return render(request=request, template_name='almocos/menu.html', context={"form":form, "menu":menu})
class edit_menu(UpdateView):
	success_message='Menu alterado com sucesso'
	model = menus
	form_class = NewMenuForm
	template_name = 'almocos/edit_menu.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_menu,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("almocos:menu")
def delete_menu(request, id):
	menu = menus.objects.get(id=id)
	menu.delete()
	messages.success(request, "Menu eliminado com sucesso")
	return redirect("almocos:menu")

def ementa(request):
	ementa = ementas.objects.all()  
	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
	menu = menus.objects.all() 
	myFilter = FilterEmentas(request.GET, queryset=ementa)
	ementa = myFilter.qs

	if request.method == 'POST':
		form = NewEmentaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Ementa adicioniada com sucesso")
		else:
			return render(request=request, template_name='almocos/ementa.html', context={"form":form, 'ementa':ementa, 'myFilter':myFilter, "inscricao":inscricao, "menu":menu})
		return redirect("almocos:ementa")
	else:
		form = NewEmentaForm()
	return render(request=request, template_name='almocos/ementa.html', context={"form":form, 'ementa':ementa, 'myFilter':myFilter, "inscricao":inscricao, "menu":menu})
class edit_ementa(UpdateView):
	success_message='Ementa alterada com sucesso'
	model = ementas
	form_class = NewEmentaForm
	template_name = 'almocos/edit_ementa.html'
	def post(self, request, **kwargs):
            messages.success(self.request, self.success_message)
            return super(edit_ementa,self).post(request,**kwargs)
	def get_success_url(self, **kwargs):
		return reverse("almocos:ementa")
def delete_ementa(request, id):
	ementa = ementas.objects.get(id=id)
	ementa.delete()
	messages.success(request, "Ementa eliminada com sucesso")
	return redirect("almocos:ementa")
