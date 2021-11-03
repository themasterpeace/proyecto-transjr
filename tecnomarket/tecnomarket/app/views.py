from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
# Create your views here.
def home(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data) 

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    
    return render(request, 'app/contacto.html', data) 

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Informacion guardada corectamente"
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    productos = producto.objects.all()
    
    data = {
        'productos': productos
    }
    
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):
    
    Producto = get_object_or_404(producto, id=id)
    
    data = {
        'form' : ProductoForm(instance=Producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=Producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificacion Exitosa")
            return redirect(to="listar_productos")
        data["form"] = formulario
    
    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    Producto = get_object_or_404(producto, id=id)
    Producto.delete()
    messages.success(request, "Informacion Eliminada permanentemente")
    return redirect(to="listar_productos")
