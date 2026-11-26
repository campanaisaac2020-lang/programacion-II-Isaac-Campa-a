from django.db import models
from django.urls import reverse


class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=100)
    fundada = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('marca_detail', args=[self.pk])
