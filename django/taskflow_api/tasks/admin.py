# tasks/admin.py
from django.contrib import admin
from .models import Project, Task, Telefonos


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date", "created_at")
    list_filter = ("status", "project")
    search_fields = ("title", "description")


@admin.register(Telefonos)
class TelefonosAdmin(admin.ModelAdmin):
    list_display = ("Tipo_de_telefono", "Marca_Telefono", "Gamma_Telefono", "Valor_Telefono", "created_at")
    search_fields = ("Marca_Telefono",)