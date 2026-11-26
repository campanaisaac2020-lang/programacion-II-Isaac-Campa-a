from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import EquipoMovilForm
from ..models import EquipoMovil

def equipo_list(request):
    pista = request.GET.get('pista', '').strip()
    equipos = EquipoMovil.objects.all()
    if pista:
        equipos = equipos.filter(Q(marca__icontains=pista)|Q(modelo__icontains=pista)|Q(descripcion__icontains=pista))
    es_administrador = request.user.is_authenticated and (
        request.user.is_superuser
        or request.user.groups.filter(name='administradores').exists()
    )
    return render(request, 'ventas/equipos/equipo_list.html', {
        'equipos': equipos,
        'pista': pista,
        'es_administrador': es_administrador,
    })

def equipo_detail(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    es_administrador = request.user.is_authenticated and (
        request.user.is_superuser
        or request.user.groups.filter(name='administradores').exists()
    )
    return render(request, 'ventas/equipos/equipo_detail.html', {
        'equipo': equipo,
        'es_administrador': es_administrador,
    })

@login_required
@permission_required('ventas.add_equipomovil', raise_exception=True)
def equipo_create(request):
    form = EquipoMovilForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        equipo = form.save(commit=False)
        equipo.creado_por = request.user
        equipo.save()
        form.save_m2m()
        messages.success(request, 'Equipo creado exitosamente.')
        return redirect('equipo_list')
    return render(request, 'ventas/equipos/formulario.html', {'form': form})

@login_required
@permission_required('ventas.change_equipomovil', raise_exception=True)
def equipo_update(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    if not request.user.has_perm('ventas.change_equipomovil') or (
        not request.user.groups.filter(name='administradores').exists()
        and equipo.creado_por_id != request.user.pk
    ):
        raise PermissionDenied
    form = EquipoMovilForm(request.POST or None, instance=equipo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Equipo editado exitosamente.')
        return redirect('equipo_detail', pk=equipo.pk)
    return render(request, 'ventas/equipos/formulario.html', {'form': form})

@login_required
@permission_required('ventas.delete_equipomovil', raise_exception=True)
def equipo_delete(request, pk):
    equipo = get_object_or_404(EquipoMovil, pk=pk)
    if (
        not request.user.groups.filter(name='administradores').exists()
        and equipo.creado_por_id != request.user.pk
    ):
        raise PermissionDenied
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente.')
        return redirect('equipo_list')
    return render(request, 'ventas/equipos/equipo_confirm_delete.html', {'equipo': equipo})
