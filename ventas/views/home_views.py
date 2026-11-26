from django.shortcuts import render
from ..models import Marca

def home(request):
    return render(request, 'ventas/home.html', {
        'marcas_disponibles': Marca.objects.filter(disponible=True).count(),
    })
