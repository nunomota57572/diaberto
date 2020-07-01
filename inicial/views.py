from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from datetime import date
import datetime
from django.views.generic import UpdateView
from django.urls import reverse
from inscricoes.models import inscricao1

def inicial(request):
	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
	return render(request=request, template_name='inicial/inicial.html', context={"inscricao":inscricao})
