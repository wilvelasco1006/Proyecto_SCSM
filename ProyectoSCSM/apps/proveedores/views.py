from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProveedorForm
from django.contrib import messages

@login_required
def registrar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor guardado con éxito")
            return redirect('registrar_proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor/registrar_proveedor.html', {'form': form})
