from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..models import EquipoMovil

class EquipoMovilForm(forms.ModelForm):
    class Meta:
        model = EquipoMovil
        fields = [
            'marca',
            'modelo',
            'categoria',
            'fabricante',
            'anio',
            'fecha_lanzamiento',
            'almacenamiento_gb',
            'precio',
            'estado',
            'accesorios',
            'descripcion',
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'min': 1980}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'almacenamiento_gb': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def clean_anio(self):
        anio = self.cleaned_data['anio']
        if anio > timezone.localdate().year:
            raise ValidationError('El año del equipo no puede ser futuro.')
        return anio
