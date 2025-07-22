from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cafe, name='registrar_cafe'),
    path('editar/<int:id>/', views.editar_cafe, name='editar_cafe'),
    path('eliminar/<int:id>/', views.eliminar_cafe, name='eliminar_cafe'),
]