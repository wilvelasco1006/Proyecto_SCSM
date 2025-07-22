from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_venta, name='registrar_venta'),
    path('listar/', views.listar_ventas, name='listar_ventas'),
    path('detalle/<uuid:id>/', views.detalle_venta, name='detalle_venta'),
    path('factura/<uuid:id>/', views.generar_factura, name='generar_factura'),
    path('cliente-info/<int:cliente_id>/', views.obtener_info_cliente, name='obtener_info_cliente'),
]