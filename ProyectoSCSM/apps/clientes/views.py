from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ClienteForm
from .models import Cliente

def es_admin(user):
    return user.is_staff

@login_required
def registrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado con éxito")
            return redirect('registrar_cliente')
    else:
        form = ClienteForm()

    # Listar clientes activos
    clientes = Cliente.objects.filter(is_active=True)

    return render(request, 'cliente/registrar_cliente.html', {'form': form, 'clientes': clientes})

'''
@login_required
@user_passes_test(es_admin)
def eliminar_cliente(request, cedula):
    cliente = get_object_or_404(Cliente, cedula=cedula)
    cliente.is_active = False
    cliente.save()
    messages.success(request, "Cliente eliminado con éxito")
    return redirect('registrar_cliente')
'''