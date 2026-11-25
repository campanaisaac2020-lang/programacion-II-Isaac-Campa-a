from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import EquipoMovilForm
from ..models import EquipoMovil

def equipo_list(request):
    pista = request.GET.get('pista', '').strip()
    equipos = EquipoMovil.objects.all()
    if pista:
        equipos = equipos.filter(Q(marca__icontains=pista)|Q(modelo__icontains=pista)|Q(descripcion__icontains=pista))
    return render(request, 'ventas/equipos/equipo_list.html', {'equipos': equipos, 'pista': pista})

def equipo_detail(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    return render(request, 'ventas/equipos/equipo_detail.html', {'equipo': equipo})

def equipo_create(request):
    form = EquipoMovilForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Equipo creado exitosamente.')
        return redirect('equipo_list')
    return render(request, 'ventas/equipos/formulario.html', {'form': form})

def equipo_update(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    form = EquipoMovilForm(request.POST or None, instance=equipo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Equipo editado exitosamente.')
        return redirect('equipo_detail', pk=equipo.pk)
    return render(request, 'ventas/equipos/formulario.html', {'form': form})

def equipo_delete(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente.')
        return redirect('equipo_list')
    return render(request, 'ventas/equipos/equipo_confirm_delete.html', {'equipo': equipo})
