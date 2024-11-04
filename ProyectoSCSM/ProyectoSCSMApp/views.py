from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ProveedorForm, CafeForm, ClienteForm
from .models import Proveedor
from django.contrib import messages #importamos messages para poder poner mensajes de confirmacion etc
def home(request):
    return render(request, 'home.html')  # Renderiza la plantilla de inicio

@login_required
def ingresar(request):
    return render(request, 'ingresar.html')  # Renderiza la plantilla de ingreso

def exit(request):
    logout(request)  # Cierra sesión del usuario
    return redirect('home')  # Redirige a la página de inicio

def register(request):
    data = {
        'form': CustomUserCreationForm()  # Crea un nuevo formulario de registro
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)  # Recibe los datos del formulario

        if user_creation_form.is_valid():  # Verifica si el formulario es válido
            user_creation_form.save()  # Guarda el nuevo usuario

            # Autentica al usuario y lo inicia
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('home')  # Redirige a la página de inicio

    return render(request, 'registration/register.html', data)  # Renderiza la plantilla de registro

def registrar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Proveedor guardado con éxito") #Mensaje que muestra que se guardo con exito al provedor
            return redirect('registrar_proveedor')  # Reinicia la pagina después de guardar pa que quede n vacios los campos
    else:
        form = ProveedorForm()
    return render(request, 'registrar_proveedor.html', {'form': form})

def registrar_cafe(request):
    if request.method == "POST":
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compra de cafe registrada con éxito")
            return redirect('registrar_cafe')  # Redirige a la página de inicio después de guardar
    else:
        form = CafeForm()
    return render(request, 'registrar_cafe.html', {'form': form})

def registrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado con éxito")
            return redirect('registrar_cliente')  # Cambia este nombre a la URL donde deseas redirigir después de guardar
    else:
        form = ClienteForm()  # Esto debería estar fuera del bloque `if form.is_valid()`

    # Renderiza el formulario si es GET o si no es válido en POST
    return render(request, 'registrar_cliente.html', {'form': form})