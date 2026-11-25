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
    def test_catalog_lists_are_public(self):
        for route in (
            'equipo_list',
            'categoria_list',
        ):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)

    def test_equipment_can_be_created_without_logging_in(self):
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

        self.assertRedirects(response, reverse('equipo_list'))
