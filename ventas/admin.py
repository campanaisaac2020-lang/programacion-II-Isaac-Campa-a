from django.contrib import admin
from .models import Categoria, EquipoMovil

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')

@admin.register(EquipoMovil)
class EquipoMovilAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'estado', 'anio')
    list_filter = ('categoria', 'estado', 'anio')
    search_fields = ('marca', 'modelo', 'descripcion')
