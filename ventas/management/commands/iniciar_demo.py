from datetime import date
from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand
from ventas.models import Accesorio, Categoria, EquipoMovil, Marca

class Command(BaseCommand):
    help = 'Crea categorías y equipos de demostración'

    def handle(self, *args, **options):
        administradores, _ = Group.objects.get_or_create(name='administradores')
        consultores, _ = Group.objects.get_or_create(name='consultores')

        all_permissions = Permission.objects.filter(
            content_type__app_label='ventas',
        )
        administradores.permissions.set(all_permissions)
        consultores.permissions.clear()
        for model_name in ('categoria', 'equipomovil', 'marca', 'accesorio'):
            consultores.permissions.add(*Permission.objects.filter(
                content_type__app_label='ventas',
                content_type__model=model_name,
                codename__in=[
                    f'view_{model_name}',
                    f'add_{model_name}',
                ],
            ))
        consultores.permissions.add(*Permission.objects.filter(
            content_type__app_label='ventas',
            content_type__model__in=['categoria', 'equipomovil'],
            codename__in=['change_categoria', 'change_equipomovil'],
        ))

        superuser, _ = User.objects.get_or_create(username='admin')
        superuser.email = 'admin@ventacelulares.local'
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.set_password('Admin123!')
        superuser.save()

        administrador, _ = User.objects.get_or_create(username='administrador')
        administrador.email = 'administrador@ventacelulares.local'
        administrador.set_password('Admin123!')
        administrador.save()
        administrador.groups.set([administradores])

        consultor, _ = User.objects.get_or_create(username='consultor')
        consultor.email = 'consultor@ventacelulares.local'
        consultor.set_password('Consultor123!')
        consultor.save()
        consultor.groups.set([consultores])

        marcas = []
        for nombre, pais, fundada, descripcion, disponible in [
            ('Samsung', 'Corea del Sur', 1938, 'Fabricante de teléfonos y dispositivos electrónicos.', True),
            ('Apple', 'Estados Unidos', 1976, 'Diseña teléfonos y productos electrónicos.', True),
            ('Xiaomi', 'China', 2010, 'Marca de teléfonos y productos inteligentes.', True),
            ('Motorola', 'Estados Unidos', 1928, 'Fabricante histórico de equipos de comunicación.', False),
            ('Honor', 'China', 2013, 'Marca de teléfonos y dispositivos inteligentes.', True),
        ]:
            marcas.append(Marca.objects.update_or_create(
                nombre=nombre,
                defaults={
                    'pais_origen': pais,
                    'fundada': fundada,
                    'descripcion': descripcion,
                    'disponible': disponible,
                },
            )[0])

        accesorios = []
        for nombre, precio in [
            ('Cargador', '19.99'),
            ('Audífonos', '29.99'),
            ('Protector', '9.99'),
            ('Cable USB-C', '12.99'),
            ('Power Bank', '39.99'),
        ]:
            accesorios.append(Accesorio.objects.get_or_create(
                nombre=nombre,
                defaults={'precio': precio, 'disponible': True},
            )[0])

        categoria_nombres = ['Android', 'iPhone', 'Gama alta', 'Gama media', 'Reacondicionados']
        categorias = [
            Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={'descripcion': f'Teléfonos de categoría {nombre}.'},
            )[0]
            for nombre in categoria_nombres
        ]
        equipos = [
            ('Samsung', 'Galaxy S24', 2024, 256, '899.00', 0, 0),
            ('Apple', 'iPhone 15', 2023, 128, '999.00', 1, 1),
            ('Xiaomi', 'Redmi Note 13', 2024, 128, '299.00', 3, 2),
            ('Motorola', 'Edge 50', 2024, 256, '449.00', 2, 3),
            ('Honor', 'Magic 6', 2024, 512, '699.00', 4, 4),
        ]
        for marca, modelo, anio, almacenamiento, precio, indice_categoria, indice_marca in equipos:
            equipo, created = EquipoMovil.objects.get_or_create(
                marca=marca,
                modelo=modelo,
                defaults={
                    'categoria': categorias[indice_categoria],
                    'fabricante': marcas[indice_marca],
                    'anio': anio,
                    'fecha_lanzamiento': date(anio, 1, 15),
                    'almacenamiento_gb': almacenamiento,
                    'precio': precio,
                    'estado': EquipoMovil.Estado.DISPONIBLE,
                    'descripcion': 'Equipo de demostración.',
                    'creado_por': administrador,
                },
            )
            if created:
                equipo.accesorios.add(accesorios[indice_marca])

        self.stdout.write(self.style.SUCCESS('Datos, usuarios y grupos de demostración creados.'))
