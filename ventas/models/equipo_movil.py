from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class EquipoMovil(models.Model):
    class Estado(models.TextChoices):
        DISPONIBLE = 'disponible', 'Disponible'
        AGOTADO = 'agotado', 'No disponible'

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.PROTECT,
        related_name='equipos',
        null=True,
    )
    anio = models.PositiveSmallIntegerField(validators=[MinValueValidator(1980)])
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    almacenamiento_gb = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    estado = models.CharField(max_length=12, choices=Estado.choices, default=Estado.DISPONIBLE)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Equipo móvil'
        verbose_name_plural = 'Equipos móviles'
        ordering = ['marca', 'modelo']

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.anio})'

    def get_absolute_url(self):
        return reverse('equipo_detail', args=[self.pk])
