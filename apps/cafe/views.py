from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CafeForm
from .models import Cafe
from django.core.paginator import Paginator
from django.db.models import Q

def es_admin(user):
    return user.is_staff

@login_required
def registrar_cafe(request):
    if request.method == "POST":
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compra de café registrada con éxito")
            return redirect('registrar_cafe')
    else:
        form = CafeForm()
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    # Filtrar resultados si hay término de búsqueda
    if search_query:
        cafe_lista = Cafe.objects.filter(
            Q(datos_proveedor__nombres__icontains=search_query) | 
            Q(datos_proveedor__cedula__icontains=search_query) |
            Q(fecha_compra__icontains=search_query)
        )
    else:
        cafe_lista = Cafe.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(cafe_lista, 10)
    page = request.GET.get('page')
    cafe = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'cafe/registrar_cafe.html', {
        'form': form,
        'cafe': cafe,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_cafe(request, id):
    cafe = get_object_or_404(Cafe, id=id)
    
    if request.method == "POST":
        form = CafeForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de café actualizado con éxito")
            return redirect('registrar_cafe')
    else:
        form = CafeForm(instance=cafe)
        
    return render(request, 'cafe/editar_cafe.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_cafe(request, id):
    cafe = get_object_or_404(Cafe, id=id)
    
    if request.method == "POST":
        cafe.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Registro de café eliminado con éxito")
        return redirect('registrar_cafe')
        
    return render(request, 'cafe/confirmar_eliminacion.html', {'cafe': cafe})
