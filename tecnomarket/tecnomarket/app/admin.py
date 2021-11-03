from django.contrib import admin
from .models import marca, producto, Contacto
# Register your models here.

class productoadmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca","nuevo", "precio"]
    list_per_page = 5    
      





admin.site.register(marca)
admin.site.register(producto, productoadmin)
admin.site.register(Contacto)

