from goku.models import *
from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(Rutas)
admin.site.register(Departamento)
admin.site.register(Municipios)
admin.site.register(Clientes)
admin.site.register(Vendedor)
admin.site.register(Boletadeposito)
admin.site.register(Ingreso_bodega)
admin.site.register(Ingreso_guias)

