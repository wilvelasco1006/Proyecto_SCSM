from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cafe, name='registrar_cafe'),
]