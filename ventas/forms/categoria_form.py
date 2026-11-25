from django import forms
from django.core.exceptions import ValidationError
from ..models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}), 'descripcion': forms.Textarea(attrs={'class':'form-control','rows':3})}
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre
