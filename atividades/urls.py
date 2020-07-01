from django.urls import path
from . import views

app_name = "atividades"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("showatividade/<int:id>", views.AtividadeView, name="showatividade"),
	path("createActividade/", views.createActividade, name="createActividade"),
    path("delete_atividade/<delete>", views.deleteatividadeAction, name="delete"),
    path("atividades/<int:pk>/update", views.AtividadeUpdateView.as_view(), name="update"),
    path("<int:pk>/validar_Atividade", views.validar_Atividade, name="validar"),
    path("<int:pk>/rejeitar_Atividade", views.rejeitar_Atividade, name="rejeitar"),
]
