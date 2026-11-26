# tasks/admin.py
from django.contrib import admin
from .models import Project, Telefonos


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Telefonos)
class TelefonosAdmin(admin.ModelAdmin):
    list_display = ("Tipo_de_telefono", "Marca_Telefono", "Gamma_Telefono", "Valor_Telefono", "created_at")
    search_fields = ("Marca_Telefono",)