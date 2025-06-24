from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import (
    CafeTrillardoForm, CafeTostadoForm, CafeMolidoForm, CafeEmpacadoForm
)
from .models import CafeTrillado, CafeTostado, CafeMolido, CafeEmpacado
from django.core.paginator import Paginator
from django.db.models import Q

def es_admin(user):
    return user.is_staff

# ---- CAFÉ TRILLADO ----
@login_required
def registrar_trillado(request):
    if request.method == "POST":
        form = CafeTrillardoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proceso de café trillado registrado con éxito")
            return redirect('registrar_trillado')
    else:
        form = CafeTrillardoForm()
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    if search_query:
        trillado_lista = CafeTrillado.objects.filter(
            Q(responsable__icontains=search_query) | 
            Q(fecha__icontains=search_query)
        )
    else:
        trillado_lista = CafeTrillado.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(trillado_lista, 10)
    page = request.GET.get('page')
    trillado = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'proceso/registrar_trillado.html', {
        'form': form,
        'trillado': trillado,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_trillado(request, id):
    trillado = get_object_or_404(CafeTrillado, id=id)
    
    if request.method == "POST":
        form = CafeTrillardoForm(request.POST, instance=trillado)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de café trillado actualizado con éxito")
            return redirect('registrar_trillado')
    else:
        form = CafeTrillardoForm(instance=trillado)
        
    return render(request, 'proceso/editar_trillado.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_trillado(request, id):
    trillado = get_object_or_404(CafeTrillado, id=id)
    
    if request.method == "POST":
        trillado.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Registro de café trillado eliminado con éxito")
        return redirect('registrar_trillado')
        
    return render(request, 'proceso/confirmar_eliminacion.html', {
        'proceso': trillado,
        'tipo': 'café trillado',
        'ruta_regreso': 'registrar_trillado'
    })

# ---- CAFÉ TOSTADO ----
@login_required
def registrar_tostado(request):
    if request.method == "POST":
        form = CafeTostadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proceso de café tostado registrado con éxito")
            return redirect('registrar_tostado')
    else:
        form = CafeTostadoForm()
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    if search_query:
        tostado_lista = CafeTostado.objects.filter(
            Q(responsable__icontains=search_query) | 
            Q(fecha__icontains=search_query)
        )
    else:
        tostado_lista = CafeTostado.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(tostado_lista, 10)
    page = request.GET.get('page')
    tostado = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'proceso/registrar_tostado.html', {
        'form': form,
        'tostado': tostado,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_tostado(request, id):
    tostado = get_object_or_404(CafeTostado, id=id)
    
    if request.method == "POST":
        form = CafeTostadoForm(request.POST, instance=tostado)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de café tostado actualizado con éxito")
            return redirect('registrar_tostado')
    else:
        form = CafeTostadoForm(instance=tostado)
        
    return render(request, 'proceso/editar_tostado.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_tostado(request, id):
    tostado = get_object_or_404(CafeTostado, id=id)
    
    if request.method == "POST":
        tostado.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Registro de café tostado eliminado con éxito")
        return redirect('registrar_tostado')
        
    return render(request, 'proceso/confirmar_eliminacion.html', {
        'proceso': tostado,
        'tipo': 'café tostado',
        'ruta_regreso': 'registrar_tostado'
    })

# ---- CAFÉ MOLIDO ----
@login_required
def registrar_molido(request):
    if request.method == "POST":
        form = CafeMolidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proceso de café molido registrado con éxito")
            return redirect('registrar_molido')
    else:
        form = CafeMolidoForm()
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    if search_query:
        molido_lista = CafeMolido.objects.filter(
            Q(responsable__icontains=search_query) | 
            Q(fecha__icontains=search_query)
        )
    else:
        molido_lista = CafeMolido.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(molido_lista, 10)
    page = request.GET.get('page')
    molido = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'proceso/registrar_molido.html', {
        'form': form,
        'molido': molido,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_molido(request, id):
    molido = get_object_or_404(CafeMolido, id=id)
    
    if request.method == "POST":
        form = CafeMolidoForm(request.POST, instance=molido)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de café molido actualizado con éxito")
            return redirect('registrar_molido')
    else:
        form = CafeMolidoForm(instance=molido)
        
    return render(request, 'proceso/editar_molido.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_molido(request, id):
    molido = get_object_or_404(CafeMolido, id=id)
    
    if request.method == "POST":
        molido.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Registro de café molido eliminado con éxito")
        return redirect('registrar_molido')
        
    return render(request, 'proceso/confirmar_eliminacion.html', {
        'proceso': molido,
        'tipo': 'café molido',
        'ruta_regreso': 'registrar_molido'
    })

# ---- CAFÉ EMPACADO ----
@login_required
def registrar_empacado(request):
    if request.method == "POST":
        form = CafeEmpacadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proceso de café empacado registrado con éxito")
            return redirect('registrar_empacado')
    else:
        form = CafeEmpacadoForm()
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    if search_query:
        empacado_lista = CafeEmpacado.objects.filter(
            Q(responsable__icontains=search_query) | 
            Q(fecha__icontains=search_query)
        )
    else:
        empacado_lista = CafeEmpacado.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(empacado_lista, 10)
    page = request.GET.get('page')
    empacado = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'proceso/registrar_empacado.html', {
        'form': form,
        'empacado': empacado,
        'es_administrador': es_administrador,
        'search_query': search_query
    })

@login_required
@user_passes_test(es_admin)
def editar_empacado(request, id):
    empacado = get_object_or_404(CafeEmpacado, id=id)
    
    if request.method == "POST":
        form = CafeEmpacadoForm(request.POST, instance=empacado)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro de café empacado actualizado con éxito")
            return redirect('registrar_empacado')
    else:
        form = CafeEmpacadoForm(instance=empacado)
        
    return render(request, 'proceso/editar_empacado.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminar_empacado(request, id):
    empacado = get_object_or_404(CafeEmpacado, id=id)
    
    if request.method == "POST":
        empacado.delete()  # Usa el método sobrescrito que hace borrado lógico
        messages.success(request, "Registro de café empacado eliminado con éxito")
        return redirect('registrar_empacado')
        
    return render(request, 'proceso/confirmar_eliminacion.html', {
        'proceso': empacado,
        'tipo': 'café empacado',
        'ruta_regreso': 'registrar_empacado'
    })

# Create your views here.
