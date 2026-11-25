from datetime import date
from django.core.management.base import BaseCommand
from ventas.models import Categoria, EquipoMovil

class Command(BaseCommand):
    help = 'Crea categorías y equipos de demostración'

    def handle(self, *args, **options):
        categoria_nombres = ['Android', 'iPhone', 'Gama alta', 'Gama media', 'Reacondicionados']
        categorias = [
            Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={'descripcion': f'Teléfonos de categoría {nombre}.'},
            )[0]
            for nombre in categoria_nombres
        ]
        equipos = [
            ('Samsung', 'Galaxy S24', 2024, 256, '899.00', 0),
            ('Apple', 'iPhone 15', 2023, 128, '999.00', 1),
            ('Xiaomi', 'Redmi Note 13', 2024, 128, '299.00', 3),
            ('Motorola', 'Edge 50', 2024, 256, '449.00', 2),
            ('Honor', 'Magic 6', 2024, 512, '699.00', 4),
        ]
        for marca, modelo, anio, almacenamiento, precio, indice_categoria in equipos:
            EquipoMovil.objects.get_or_create(
                marca=marca,
                modelo=modelo,
                defaults={
                    'categoria': categorias[indice_categoria],
                    'anio': anio,
                    'fecha_lanzamiento': date(anio, 1, 15),
                    'almacenamiento_gb': almacenamiento,
                    'precio': precio,
                    'estado': EquipoMovil.Estado.DISPONIBLE,
                    'descripcion': 'Equipo de demostración.',
                },
            )
        self.stdout.write(self.style.SUCCESS('Categorías y equipos de demostración creados.'))
