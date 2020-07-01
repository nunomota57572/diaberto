from django.urls import path
from . import views 

app_name = "notificacao"

urlpatterns = [

    path('', views.getNotificacao, name="notificacao"),
    path('enviar/', views.postNotificacao, name="notificacao2"),
    path('ajax/conteudo/', views.conteudo, name="notificacao3"),
    path('enviadas/', views.getEnviNotificacao, name="notificacao4"),





 
]
