from django.urls import path
from . import views 

app_name = "transportes"

urlpatterns = [
    path('autocarro/', views.autocarro, name="autocarro"),
    path('autocarro/<int:id>', views.percurso_autocarro, name="percurso_autocarro"),    
    path('autocarro/<int:pk>/edit', views.edit_autocarro.as_view(), name="edit_autocarro"),  
    path('autocarro/<int:id>/delete', views.delete_autocarro, name="delete_autocarro"),    

    path('percurso/', views.percurso, name="percurso"),
    path('percurso/<int:id>/', views.atribuir_a_percurso, name="atribuir_a_percurso"),  
    path('percurso/<int:pk>/edit', views.edit_percurso.as_view(), name="edit_percurso"),  
    path('percurso/<int:id>/delete', views.delete_percurso, name="delete_percurso"),    
]
