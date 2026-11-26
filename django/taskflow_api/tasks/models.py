from django.db import models

# tasks/models.py
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Telefonos(models.Model):
    Tipo_de_telefono = models.CharField(max_length=100)
    Marca_Telefono = models.TextField(blank=True)
    Gamma_Telefono = models.TextField(blank=True)
    Valor_Telefono = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Marca_Telefono} {self.Tipo_de_telefono}" 
    