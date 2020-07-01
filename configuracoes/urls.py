from django.urls import path
from . import views 

app_name = "configuracoes"

urlpatterns = [
    path('geral/', views.geral, name="geral"),
    path('geral/new', views.new_geral, name="new_geral"),
    path('geral/<int:pk>/edit', views.edit_geral.as_view(), name="edit_geral"),
    path('geral/<int:id>/delete', views.delete_geral, name="delete_geral"),

    path('horarios_tranportes/', views.horario_transporte, name="horario_transporte"),
    path('horarios_tranportes/delete', views.delete_horario_transporte, name="delete_horario_transporte"),

    path('horarios_atividades/', views.horario_atividade, name="horario_atividade"),
    path('horarios_atividades/delete', views.delete_horario_atividade, name="delete_horario_atividade"),

    path('escolas/', views.escola, name="escola"),
    path('escolas/<int:pk>/edit', views.edit_escola.as_view(), name="edit_escola"),
    path('escolas/<int:id>/delete', views.delete_escola, name="delete_escola"),

    path('unidades_organicas/', views.uo, name="uo"),
    path('unidades_organicas/<int:pk>/edit', views.edit_uo.as_view(), name="edit_uo"),
    path('unidades_organicas/<int:id>/delete', views.delete_uo, name="delete_uo"),

    path('departamentos/', views.departamento, name="departamento"),
    path('departamentos/<int:pk>/edit', views.edit_departamento.as_view(), name="edit_departamento"),
    path('departamentos/<int:id>/delete', views.delete_departamento, name="delete_departamento"),

    path('cursos/', views.curso, name="curso"),
    path('cursos/<int:pk>/edit', views.edit_curso.as_view(), name="edit_curso"),
    path('cursos/<int:id>/delete', views.delete_curso, name="delete_curso"),
]
