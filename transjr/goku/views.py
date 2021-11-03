from django.http import request 
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render(request, 'goku/home.html')

def ingreso_bodega(request):
    return render(request, 'goku/ingreso_bod.html')

def salida_bodega(request):
    return render(request, 'goku/salida_bod.html')

def consulta(request):
    return render(request, 'goku/consulta.html')

def vendedores(request):
    data = {
        'form': VendedorForm()
    }
    
    if request.method == 'POST':
        formulario = VendedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Vendedor Agregado con exito"
        else:
            data["form"] = formulario
    return render(request, 'goku/vendedores.html', data)

def municipio(request):
    data = {
        'form': MunicipioForm()
    }
    return render(request, 'goku/municipio.html', data)

def rutas(request):
    data = {
        'form': RutasForm()
    }
    return render(request, 'goku/rutas.html', data)

def nuevo_cliente(request):
    data ={
        'form': NuevoClienteForm()
    }
    return render(request, 'goku/nuevo_cliente.html', data)

def departamento(request):
    data = {
        'form': DepartamentoForm()
    }
    if request.method == 'POST':
        formulario = DepartamentoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Departamento Agregado con exito"
        else:
            data["form"] = formulario
    return render(request, 'goku/departamento.html', data)

def pilotos(request):
    data = {
        'form': PilotosForm()
    }
    return render(request, 'goku/pilotos.html', data)

def ingresogui(request):
    data = {
        'form': IngresoForm()
    }
    if request.method == 'POST':
        formulario = IngresoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guia ingresada correctamente"
        else:
            data["form"] = formulario
    return render(request, 'goku/ingreso_guias.html', data)

def ingresobod(request):
    data = {
        'form': IngresoBodegaForm()
    }
    return render(request, 'goku/ingreso_bod.html', data)

def boletadeposito(request):
    data = {
        'form':BoletaForm()
    }
    return render(request, 'goku/boletas.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            #redirigir al home 
            return redirect(to="home")
        data["form"]= formulario
    return render(request, 'registration/registro.html', data)

