from django import forms
from django.core.exceptions import ValidationError
from ..models import Accesorio


class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['nombre', 'precio', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero.')
        return precio
