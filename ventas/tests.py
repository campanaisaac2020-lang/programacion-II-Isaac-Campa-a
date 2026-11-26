from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .forms import EquipoMovilForm
from .models import Categoria


class EquipoMovilFormTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Prueba')

    def equipo_data(self, anio):
        return {
            'marca': 'Marca de prueba',
            'modelo': 'Modelo de prueba',
            'categoria': self.categoria.pk,
            'anio': anio,
            'almacenamiento_gb': 128,
            'precio': '299.99',
            'estado': 'disponible',
            'descripcion': '',
        }

    def test_accepts_entered_brand_and_current_or_past_year(self):
        form = EquipoMovilForm(data=self.equipo_data(timezone.localdate().year))

        self.assertTrue(form.is_valid(), form.errors)

    def test_rejects_future_year(self):
        form = EquipoMovilForm(
            data=self.equipo_data(timezone.localdate().year + 1)
        )

        self.assertFalse(form.is_valid())
        self.assertIn('anio', form.errors)


class PublicCatalogViewsTests(TestCase):
    def test_authentication_pages_render(self):
        for route in ('login', 'registro'):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)

    def test_catalog_lists_are_public(self):
        for route in (
            'equipo_list',
            'categoria_list',
            'marca_list',
            'accesorio_list',
        ):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)

    def test_equipment_creation_requires_login(self):
        category = Categoria.objects.create(nombre='Teléfonos')
        data = {
            'marca': 'Marca de prueba',
            'modelo': 'Modelo de prueba',
            'categoria': category.pk,
            'anio': timezone.localdate().year,
            'almacenamiento_gb': 128,
            'precio': '299.99',
            'estado': 'disponible',
            'descripcion': '',
        }

        response = self.client.post(reverse('create_equipo'), data)

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('create_equipo')}",
        )

    def test_logout_rejects_get_requests(self):
        user = User.objects.create_user(username='logout-user', password='test-pass')
        self.client.force_login(user)

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 405)


class OwnershipPermissionTests(TestCase):
    def setUp(self):
        self.consultores = Group.objects.create(name='consultores_test')
        permissions = Permission.objects.filter(
            content_type__app_label='ventas',
            codename__in=[
                'add_categoria',
                'change_categoria',
                'delete_categoria',
                'add_equipomovil',
                'change_equipomovil',
                'delete_equipomovil',
            ],
        )
        self.consultores.permissions.set(permissions)

        self.owner = User.objects.create_user(username='owner', password='test-pass')
        self.other = User.objects.create_user(username='other', password='test-pass')
        self.owner.groups.add(self.consultores)
        self.other.groups.add(self.consultores)
        self.categoria = Categoria.objects.create(
            nombre='Teléfonos',
            creado_por=self.owner,
        )

    def test_owner_can_edit_category(self):
        self.client.force_login(self.owner)

        response = self.client.post(
            reverse('categoria_update', args=[self.categoria.pk]),
            {'nombre': 'Celulares', 'descripcion': 'Actualizada'},
        )

        self.assertRedirects(response, reverse('categoria_list'))
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nombre, 'Celulares')

    def test_other_consultant_cannot_edit_or_delete_category(self):
        self.client.force_login(self.other)

        edit_response = self.client.get(
            reverse('categoria_update', args=[self.categoria.pk])
        )
        delete_response = self.client.post(
            reverse('categoria_delete', args=[self.categoria.pk])
        )

        self.assertEqual(edit_response.status_code, 403)
        self.assertEqual(delete_response.status_code, 403)
        self.assertTrue(Categoria.objects.filter(pk=self.categoria.pk).exists())

    def test_category_actions_are_hidden_for_non_owner(self):
        self.client.force_login(self.other)

        response = self.client.get(reverse('categoria_list'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, reverse('categoria_update', args=[self.categoria.pk]))

    def test_category_delete_uses_shared_confirmation_template(self):
        self.client.force_login(self.owner)

        response = self.client.get(
            reverse('categoria_delete', args=[self.categoria.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Eliminar categoría')
        self.assertContains(response, reverse('categoria_list'))
