from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse
from .models import inscricao1, inscricao_atividades
from .forms import NewInscricaoForm, NewInscricaoForm1, NewEditInscricaoForm
from atividades.models import atividade, sessao
from utilizador.models import utilizador
from .filters import FilterInscricao1, FilterAtividades
from notificacao.models import Notificacao
from notificacao.forms import AutoNotif

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def inscricaos(request):
	ins = inscricao1.objects.all()
	myFilter = FilterInscricao1(request.GET, queryset=ins)
	ins = myFilter.qs
	# print(inscricao1.objects.all())
	sess = inscricao_atividades.objects.filter(inscricaoID__UtilizadorID=request.user.id)    # !!!! ESTA MERDA MANDA TODOS !!!!
	try:
		ins1 = inscricao1.objects.get(UtilizadorID=request.user.id)
	except:
		ins1 = 'a'
	return render(request=request, template_name='inscricoes/inscricao.html', context={'inscricao':ins, 'ins1':ins1, "myFilter": myFilter, "sess": sess})

def createinscricao(request):
	if request.user.TipoUtilizador == "Participante":
		if request.method == 'POST':
			form = NewInscricaoForm(request.POST)
			if form.is_valid():
				form.save(commit= False)
				form.instance.Precisa_Transporte=False
				form.instance.UtilizadorID=request.user
				form.save()
				messages.success(request, "Inscrição realizada com sucesso")
				return redirect("inscricoes:inscricao")
			else:
				return render(request= request, template_name= "inscricoes/criarinscricao.html", context = {"form":form})
			return redirect("inscricoes:inscricao")
		else:
			form = NewInscricaoForm()
		return render(request= request, template_name= "inscricoes/criarinscricao.html", context = {"form":form})
	else:
		return redirect("inscricoes:inscricao")

def selecionar_atividades(request):
	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)

	atividades = atividade.objects.filter(Estado = 'Aceite')
	myFilter = FilterAtividades(request.GET, queryset=sessao.objects.filter(Atividade__Estado='Aceite'))
	if request.user.TipoUtilizador == "Participante":
		if request.method == 'POST':
			form = NewInscricaoForm1(request.POST)
			if form.is_valid():
				form.save(commit= False)
				form.instance.inscricaoID = inscricao1.objects.get(UtilizadorID=request.user.id)
				list_atividades = request.POST.getlist('atividades[]')
				form.save()
				messages.success(request, "Atividades adicionadas com sucesso")
				return redirect("inscricoes:ver_atividades")
		return render(request= request,
		template_name= "inscricoes/selecionaratividades.html",
		context = {"inscricao":inscricao, "myFilter": myFilter})
	else:
		return render(request= request,
		template_name= "inscricoes/selecionaratividades.html",
		context = {"atividades": atividades, "inscricao":inscricao})

def ver_atividades(request):
	atv = atividade.objects.all()
	myFilter = FilterAtividades(request.GET, queryset=atv)
	atv = myFilter.qs

	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
	sess = sessao.objects.all()
	ins_atv = inscricao_atividades.objects.filter(inscricaoID=inscricao1.objects.get(UtilizadorID=request.user.id))
	return render(request=request, template_name='inscricoes/ver_atividades.html', context= {"atividade": atv, "sessao": sess, "inscricao_atividades": ins_atv, "inscricao": inscricao, "myFilter": myFilter} )

def deleteinscricaoAction(request, id):
	if request.user.TipoUtilizador == "Participante":
		this_user = inscricao1.objects.get(id=id)
		this_user.delete()
		messages.success(request, "Inscrição eliminada com sucesso")
		return redirect("inscricoes:inscricao")
	else:
		return redirect("inicial:inicial")


def ver_inscricao(request, id):
	inscricao = inscricao1.objects.get(id=id)
	sess = inscricao_atividades.objects.filter(inscricaoID = inscricao) 

	return render(request=request,
                  template_name='inscricoes/ver_inscricao.html',
                  context={"inscricao": inscricao, "sess": sess })


class editar_inscricao(UpdateView):
	success_message='Inscrição alterada com sucesso'
	model = inscricao1
	form_class = NewEditInscricaoForm
	template_name = 'inscricoes/edit_inscricao.html'

	def get_success_url(self, **kwargs):
		return reverse("inscricoes:inscricao")

def ver_atividadeind(request, id):
	inscricao = ''
	if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
		inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)

	this_atividade = atividade.objects.get(id=id)
	this_session = sessao.objects.get(Atividade__id=id)

	return render(request=request,
	template_name='inscricoes/ver_atividadeind.html',
	context={"atividade": this_atividade, "sessao": this_session, "inscricao": inscricao})

def deleteA(request):
	if request.user.TipoUtilizador == "Participante":
		id=request.GET.get("iaid")
		id2=request.GET.get("aid")
		something = inscricao_atividades.objects.get(id=id)
		something.delete()
		messages.success(request, "Atividade removida com sucesso")
		Participantes = []
		Participantes = utilizador.objects.filter(TipoUtilizador="Participante").exclude(id=request.user.id).values_list('id', flat=True)
		for x in Participantes:
			notif = AutoNotif(request.POST)
			notif.instance.autorid=utilizador.objects.get(id=1)
			notif.instance.is_read=0
			notif.instance.assunto="Vagas disponiveis"
			notif.instance.descricao="A atividade {} possui novas vagas.".format(atividade.objects.get(id=id2).Nome_actividade)
			notif.instance.remetenteid=utilizador.objects.get(id=x)
			notif.save()
		return HttpResponse()
	else:
		return redirect("inicial:inicial")
