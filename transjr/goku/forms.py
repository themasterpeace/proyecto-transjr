from django import forms
from django.db.models import fields
from django.forms import widgets
from goku.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VendedorForm(forms.ModelForm):
    
    class Meta:
        model = Vendedor
        fields = '__all__'
        widgets = {
            "fechacrea": forms.SelectDateWidget()
        }

class MunicipioForm(forms.ModelForm):
    
    class Meta:
        model = Municipios
        fields ='__all__'
        
class RutasForm(forms.ModelForm):
    
    class Meta:
        model = Rutas
        fields = '__all__'
        
class NuevoClienteForm(forms.ModelForm):
    
    class Meta:
        model = Clientes
        fields = '__all__'
        
class DepartamentoForm(forms.ModelForm):
    
    class Meta:
        model = Departamento
        fields = '__all__'
        
class PilotosForm(forms.ModelForm):
    
    class Meta:
        model = Pilotos
        fields ='__all__'

class IngresoForm(forms.ModelForm):
    
    class Meta:
        model = Ingreso_guias
        fields = '__all__'
    
class IngresoBodegaForm(forms.ModelForm):
    
    class Meta:
        model = Ingreso_bodega
        fields = '__all__'

class BoletaForm(forms.ModelForm):
    
    class Meta:
        model = Boletadeposito
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]