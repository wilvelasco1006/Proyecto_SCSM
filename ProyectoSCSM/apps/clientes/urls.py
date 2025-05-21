from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    #path('editar/<str:cedula>/', views.editar_cliente, name='editar_cliente'),
    #path('eliminar/<str:cedula>/', views.eliminar_cliente, name='eliminar_cliente'), 
]