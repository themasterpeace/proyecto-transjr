from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('ingreso_bodega/', ingreso_bodega, name="ingreso_bodega"),
    path('salida_bodega/', salida_bodega, name="salida_bodega"),
    path('consulta/', consulta, name="consulta"),
    path('vendedores/', vendedores, name="vendedores"),
    path('municipio/', municipio, name="municipio"),
    path('rutas', rutas, name="rutas"),
    path('nuevo_cliente', nuevo_cliente, name="nuevo_cliente"),
    path('departamento', departamento, name="departamento"),
    path('pilotos', pilotos, name="pilotos"),
    path('ingreso_guias', ingresogui, name='ingreso_guias'),
    path('ingreso_bodega', ingresobod, name='ingreso_bodega'),
    path('boletas', boletadeposito, name='boletas'),
    path('registro/', registro, name='registro'),
    
]
