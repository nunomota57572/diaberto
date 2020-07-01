from django.urls import path
from . import views 

app_name = "almocos"

urlpatterns = [
    path('menu/', views.menu, name="menu"),
    #path('menu/new', views.new_menu, name="new_menu"),
    path('menu/<int:pk>/edit', views.edit_menu.as_view(), name="edit_menu"),
    path('menu/<int:id>/delete', views.delete_menu, name="delete_menu"),  

    path('ementa/', views.ementa, name="ementa"),
    #path('ementa/new', views.new_ementa, name="new_ementa"),
    path('ementa/<int:pk>/edit', views.edit_ementa.as_view(), name="edit_ementa"),
    path('ementa/<int:id>/delete', views.delete_ementa, name="delete_ementa"),   
]


