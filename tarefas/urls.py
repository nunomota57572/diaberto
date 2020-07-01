from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [

	path('atribuidas/', views.tarefas_atribuidas, name="tarefas_atribuidas"),
	path("concluir_tarefa/<int:pk>/", views.concluir_tarefa, name="concluir_tarefa"),
	path("disponibilidades/", views.disponibilidades, name="disponibilidades"),
	path("disponibilidades/create_disponibilidade/", views.create_disponibilidade, name="create_disponibilidade"),
	path("disponibilidades/edit_disponibilidade/<int:pk>/", views.edit_disponibilidade, name="edit_disponibilidade"),
    path("disponibilidades/delete_disponibilidade/<int:pk>/", views.delete_disponibilidade, name="delete_disponibilidade"),
	path('', views.homepage, name="homepage"),
    path("new_tarefa/", views.createtarefa, name="login"),
    path("colaboradores/", views.colaboradores, name="colaboradores"),
    path("tarefa/<id>", views.TarefaView, name="login"),
    path("atribuir_colab/<int:pk>/update", views.AtribuirColabUpdateView.as_view(), name="update"),
    path("atribuir_colab/<int:pk>/retirar/<delete>", views.RetirarColab, name="retirar"),
    path("delete_tarefa/<delete>", views.deletetarefaAction, name="login"),
    path("tarefa/<int:pk>/update", views.TarefaUpdateView.as_view(), name="update"),
    path("colaboradores/register", views.register, name="update")

]
