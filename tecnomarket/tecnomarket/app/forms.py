#from tecnomarket.app.views import agregar_producto
from django import forms
from django.forms import widgets
#from django.forms import fields
from .models import Contacto, producto

class ContactoForm(forms.ModelForm):
    
    #nombre = forms.CharField(widget=forms.TextInput("class":"form-control")))
    
    
    class Meta:
        model = Contacto
        #fields=["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = "__all__"
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = producto
        fields = "__all__"
        
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()        
        }
        