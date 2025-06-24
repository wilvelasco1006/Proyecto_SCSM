from django.urls import path
from . import views

urlpatterns = [
    # Café Trillado
    path('trillado/registrar/', views.registrar_trillado, name='registrar_trillado'),
    path('trillado/editar/<int:id>/', views.editar_trillado, name='editar_trillado'),
    path('trillado/eliminar/<int:id>/', views.eliminar_trillado, name='eliminar_trillado'),
    
    # Café Tostado
    path('tostado/registrar/', views.registrar_tostado, name='registrar_tostado'),
    path('tostado/editar/<int:id>/', views.editar_tostado, name='editar_tostado'),
    path('tostado/eliminar/<int:id>/', views.eliminar_tostado, name='eliminar_tostado'),
    
    # Café Molido
    path('molido/registrar/', views.registrar_molido, name='registrar_molido'),
    path('molido/editar/<int:id>/', views.editar_molido, name='editar_molido'),
    path('molido/eliminar/<int:id>/', views.eliminar_molido, name='eliminar_molido'),
    
    # Café Empacado
    path('empacado/registrar/', views.registrar_empacado, name='registrar_empacado'),
    path('empacado/editar/<int:id>/', views.editar_empacado, name='editar_empacado'),
    path('empacado/eliminar/<int:id>/', views.eliminar_empacado, name='eliminar_empacado'),
]