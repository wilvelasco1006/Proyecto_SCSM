from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CafeForm
from django.contrib import messages

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
    return render(request, 'cafe/registrar_cafe.html', {'form': form})
