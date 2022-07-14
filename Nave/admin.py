import sys
from django.contrib import admin
from .models import Categoria, Nave, Inventario


class CategoriaAdmin(admin.ModelAdmin): 
    list_display=("descripcion",)
    search_fields=("descripcion",)
    list_filter=("descripcion",)
 
class NaveAdmin(admin.ModelAdmin): 
    naves=("nombre","modelo","fabricante","categoria","anio_fabricacion","numero_llantas","numero_motores","numero_tripulantes","numero_tripulantes_max","numero_tripulantes_min","velocidad_maxima","estado","cantidadMinima")
    list_display=naves
    search_fields=("nombre","modelo","fabricante")
    list_filter: naves
class InventarioAdmin(admin.ModelAdmin): 
    inventario=("nave","cantidad")
    list_display=inventario
    search_fields=inventario
    list_filter=inventario

# Register your models here.
#admin.site.register(Categoria)
#admin.site.register(Nave)
#admin.site.register(Inventario)

#Regitro de modelos en el admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Nave, NaveAdmin)
admin.site.register(Inventario, InventarioAdmin)


