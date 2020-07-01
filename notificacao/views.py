from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Notificacao, utilizador
from .forms import NewNotificacao
from .filters import NotificacaoFilter
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from inscricoes.models import inscricao1


def getNotificacao(request):
        ident=request.user.id
        this_noti = Notificacao.objects.filter(remetenteid=ident).order_by('-criadoem')
        counter = this_noti.filter(is_read=0).count()
        this_user = request.user.Estado
        myFilter = NotificacaoFilter(request.GET, queryset=this_noti)
        this_noti = myFilter.qs
        inscricao = ''
        if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
                inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
        return render(request, "main/notificacao.html",
        context={"Notificacao": this_noti, "counter": counter,"Utilizador": this_user,"Notif": this_noti, "myFilter": myFilter, "inscricao":inscricao})

def lilbell(request):
        ident=request.user.id
        this_noti = Notificacao.objects.filter(remetenteid=ident)
        counter = this_noti.filter(is_read=0).count()
        return {"Notificacao": this_noti, "counter": counter}

def getEnviNotificacao(request):
        ident=request.user.id
        that_noti = Notificacao.objects.filter(autorid=ident)
        inscricao = ''
        if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
                inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
        return render(request,
                "main/enviada.html",
                context={"Notificacao": that_noti, "inscricao":inscricao})

def postNotificacao(request):
        if request.method == 'POST': 
                notificacao_form = NewNotificacao(request.POST)
                if notificacao_form.is_valid():
                        notificacao_form.save(commit=False)
                        notificacao_form.instance.autorid=utilizador.objects.get(id=request.user.id)
                        notificacao_form.instance.is_read=0
                        notificacao_form.save()  
                        messages.success(request, "Notificação enviada com sucesso")
                        return redirect("notificacao:notificacao")
        else:
                notificacao_form = NewNotificacao()
                inscricao = ''
                if inscricao1.objects.filter(UtilizadorID=request.user.id).count() != 0:
                        inscricao = inscricao1.objects.get(UtilizadorID=request.user.id)
        return render(request,
                "main/criar_notificacao.html",
                context={"notificacao_form":notificacao_form, "inscricao":inscricao})        


def conteudo(request):
        id=request.GET.get("id")
        updater = Notificacao.objects.get(id=id)
        updater.is_read = 1
        updater.save()
        return render(request,
        "main/test.html",
        {"notif": Notificacao.objects.get(id=id)}
        )



