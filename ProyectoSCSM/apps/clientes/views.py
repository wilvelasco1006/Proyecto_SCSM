from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from django.contrib import messages

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
    return render(request, 'cliente/registrar_cliente.html', {'form': form})