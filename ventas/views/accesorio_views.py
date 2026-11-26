from django.shortcuts import get_object_or_404, render
from ..models import Accesorio


def accesorio_list(request):
    return render(request, 'ventas/accesorios/accesorio_list.html', {'accesorios': Accesorio.objects.all()})


def accesorio_detail(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)
    return render(request, 'ventas/accesorios/accesorio_detail.html', {'accesorio': accesorio})
