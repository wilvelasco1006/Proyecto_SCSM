from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_proveedor, name='registrar_proveedor'),
    path('editar/<str:cedula>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar/<str:cedula>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]