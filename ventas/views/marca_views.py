from django.shortcuts import get_object_or_404, render
from ..models import Marca


def marca_list(request):
    return render(request, 'ventas/marcas/marca_list.html', {'marcas': Marca.objects.all()})


def marca_detail(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    return render(request, 'ventas/marcas/marca_detail.html', {'marca': marca})
