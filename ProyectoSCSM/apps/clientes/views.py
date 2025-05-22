from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ClienteForm
from .models import Cliente
from django.core.paginator import Paginator # Importar Paginator para paginación
from django.db.models import Q # Importar Q para consultas complejas
def es_admin(user): # Verifica si el usuario es administrador
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
    # Obtener parámetros de búsqueda
    search_query = request.GET.get('search', '')
    
    # Filtrar resultados si hay término de búsqueda
    if search_query:
        clientes_lista = Cliente.objects.filter(
            Q(nombres__icontains=search_query) | 
            Q(apellidos__icontains=search_query) | 
            Q(cedula__icontains=search_query)
        )
    else:
        clientes_lista = Cliente.objects.filter(is_active=True)

    
    #Paginación
    paginator = Paginator(clientes_lista, 10)  # 10 clientes por página
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    # Verificar si el usuario es administrador para mostrar botones de editar/eliminar
    es_administrador = request.user.is_staff

    return render(request, 'cliente/registrar_cliente.html', {
        'form': form,
        'clientes': clientes,
        'es_administrador': es_administrador,
        'search_query': search_query,  # Pasar la consulta de búsqueda al template
        })
@login_required
@user_passes_test(es_admin)
def editar_cliente(request, cedula):
    cliente = get_object_or_404(Cliente, cedula=cedula)# Obtener el cliente por cédula
    
    if request.method == "POST": # Si el método es POST, significa que se está editando
        form = ClienteForm(request.POST, instance=cliente)# Crear el formulario con los datos del cliente
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado con éxito")
            return redirect('registrar_cliente')
    else:
        form = ClienteForm(instance=cliente)
        
    return render(request, 'cliente/editar_cliente.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_cliente(request, cedula):
    # Obtener el cliente 
    cliente = get_object_or_404(Cliente, cedula=cedula)
    
    # Si es POST, confirmar la eliminación
    if request.method == "POST":
        cliente.delete()  # Ahora sí funciona
        messages.success(request, "Cliente eliminado con éxito")
        return redirect('registrar_cliente')
        
    # Si es GET, mostrar página de confirmación
    return render(request, 'cliente/confirmar_eliminacion.html', {'cliente': cliente})