from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ProveedorForm
from .models import Proveedor
from django.core.paginator import Paginator
from django.db.models import Q

def es_admin(user):
    return user.is_staff

@login_required
def registrar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor registrado con éxito")
            return redirect('registrar_proveedor')
    else:
        form = ProveedorForm()
    
    # Obtener parámetros de búsqueda
    search_query = request.GET.get('search', '')
    
    # Filtrar resultados si hay término de búsqueda
    if search_query:
        proveedores_lista = Proveedor.objects.filter(
            Q(nombres__icontains=search_query) | 
            Q(apellidos__icontains=search_query) | 
            Q(cedula__icontains=search_query)
        )
    else:
        proveedores_lista = Proveedor.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(proveedores_lista, 10)
    page = request.GET.get('page')
    proveedores = paginator.get_page(page)
    
    # Verificar si el usuario es administrador
    es_administrador = request.user.is_staff
    
    return render(request, 'proveedor/registrar_proveedor.html', {
        'form': form,
        'proveedores': proveedores,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_proveedor(request, cedula):
    proveedor = get_object_or_404(Proveedor, cedula=cedula)
    
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor actualizado con éxito")
            return redirect('registrar_proveedor')
    else:
        form = ProveedorForm(instance=proveedor)
        
    return render(request, 'proveedor/editar_proveedor.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_proveedor(request, cedula):
    proveedor = get_object_or_404(Proveedor, cedula=cedula)
    
    if request.method == "POST":
        proveedor.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Proveedor eliminado con éxito")
        return redirect('registrar_proveedor')
        
    return render(request, 'proveedor/confirmar_eliminacion.html', {'proveedor': proveedor})
