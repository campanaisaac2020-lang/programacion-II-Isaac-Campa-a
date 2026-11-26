from django.contrib import admin
from .models import Accesorio, Categoria, EquipoMovil, Marca

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')

@admin.register(EquipoMovil)
class EquipoMovilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'fabricante', 'precio', 'estado', 'anio')
    list_filter = ('categoria', 'fabricante', 'estado', 'anio')
    search_fields = ('marca', 'modelo', 'descripcion')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen', 'fundada')
    list_filter = ('pais_origen',)
    search_fields = ('nombre', 'pais_origen')

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre',)
