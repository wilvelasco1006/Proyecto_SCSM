from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
]