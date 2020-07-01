from django.urls import path
from . import views 

app_name = "inscricoes"

urlpatterns = [
    # path('', views.homepage, name="homepage"),
    path('inscricao/', views.inscricaos, name="inscricao"),
    path("criar_inscricao/", views.createinscricao, name="login"),
    path("selecionar_atividades/", views.selecionar_atividades, name="selecionar_atividades"),
    path("ver_atividades/", views.ver_atividades, name="ver_atividades"),
    path("ver_inscricao/<int:id>", views.ver_inscricao, name="ver_inscricao"),
    path("<int:pk>/update/", views.editar_inscricao.as_view(), name="update"),
    path("delete_inscricao/<int:id>", views.deleteinscricaoAction, name="delete_inscricao"),
    path("ver_atividadeind/<int:id>", views.ver_atividadeind, name="ver_atividadeind"),
    path('ajax/deleteA/', views.deleteA, name="deleteA"),

]
