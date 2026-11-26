from django import forms
from django.core.exceptions import ValidationError
from ..models import Marca


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'fundada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'fundada': forms.NumberInput(attrs={'class': 'form-control', 'min': 1800}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 2:
            raise ValidationError('El nombre debe tener al menos 2 caracteres.')
        return nombre
