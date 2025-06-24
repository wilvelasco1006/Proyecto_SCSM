from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse


from .models import Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaForm, VentaConDetalleForm
from apps.clientes.models import Cliente

# Verificar si el usuario es administrador
def es_admin(user):
    return user.is_staff

@login_required
def registrar_venta(request):
    if request.method == "POST":
        form = VentaConDetalleForm(request.POST)
        if form.is_valid():
            # Crear la venta
            venta = Venta(
                cliente=form.cleaned_data['cliente'],
                fecha=form.cleaned_data['fecha'],
                responsable=form.cleaned_data['responsable']
            )
            venta.save()
            
            # Crear el primer detalle
            detalle = DetalleVenta(
                venta=venta,
                tipo_cafe=form.cleaned_data['tipo_cafe'],
                cantidad=form.cleaned_data['cantidad'],
                precio_unitario=form.cleaned_data['precio_unitario']
            )
            detalle.save()
            
            # Procesar detalles adicionales
            i = 1
            while f'tipo_cafe_{i}' in request.POST:
                tipo_cafe = request.POST.get(f'tipo_cafe_{i}')
                cantidad = request.POST.get(f'cantidad_{i}')
                precio_unitario = request.POST.get(f'precio_unitario_{i}')
                
                if tipo_cafe and cantidad and precio_unitario:
                    detalle = DetalleVenta(
                        venta=venta,
                        tipo_cafe=tipo_cafe,
                        cantidad=int(cantidad),
                        precio_unitario=float(precio_unitario)
                    )
                    detalle.save()
                i += 1
            
            # Actualizar el total de la venta
            venta.actualizar_total()
            
            messages.success(request, "Venta registrada con éxito. ¿Desea generar la factura?")
            return redirect('detalle_venta', id=venta.id)
    else:
        form = VentaConDetalleForm()
    
    return render(request, 'ventas/registrar_ventas.html', {
        'form': form,
    })

@login_required
def listar_ventas(request):
    # Búsqueda
    search_query = request.GET.get('search', '')
    
    if search_query:
        ventas_lista = Venta.objects.filter(
            Q(cliente__nombres__icontains=search_query) | 
            Q(cliente__apellidos__icontains=search_query) |
            Q(cliente__cedula__icontains=search_query) |
            Q(responsable__icontains=search_query) |
            Q(fecha__icontains=search_query) |
            Q(numero_factura__icontains=search_query)
        )
    else:
        ventas_lista = Venta.objects.filter(is_active=True)
    
    # Paginación
    paginator = Paginator(ventas_lista, 10)
    page = request.GET.get('page')
    ventas = paginator.get_page(page)
    
    # Permisos
    es_administrador = request.user.is_staff
    
    return render(request, 'ventas/listar_ventas.html', {
        'ventas': ventas,
        'es_administrador': es_administrador,
        'search_query': search_query,
    })

@login_required
def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    detalles = venta.detalles.all()
    
    return render(request, 'ventas/detalle_ventas.html', {
        'venta': venta,
        'detalles': detalles,
    })

@login_required
def generar_factura(request, id):
    from weasyprint import HTML
    import tempfile
    from django.template.loader import render_to_string
    
    venta = get_object_or_404(Venta, id=id)
    detalles = venta.detalles.all()
    
    # Renderizar el HTML de la factura
    html_string = render_to_string('facturas/facturas.html', {
        'venta': venta,
        'detalles': detalles,
    })
    
    # Crear un archivo temporal para guardar el PDF
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as output:
        HTML(string=html_string).write_pdf(output)
    
    # Leer el archivo y devolverlo como respuesta
    with open(output.name, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Factura-{venta.numero_factura}.pdf"'
    
    return response

@login_required
def obtener_info_cliente(request, cliente_id):
    """Devuelve la información del cliente en formato JSON"""
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        return JsonResponse({
            'direccion': cliente.direccion,
            'cedula': cliente.cedula,
        })
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
