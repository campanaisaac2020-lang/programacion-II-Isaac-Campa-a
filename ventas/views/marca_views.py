from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import MarcaForm
from ..models import Marca


def marca_list(request):
    return render(request, 'ventas/marcas/marca_list.html', {'marcas': Marca.objects.all()})


def marca_detail(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    return render(request, 'ventas/marcas/marca_detail.html', {'marca': marca})


@login_required
@permission_required('ventas.add_marca', raise_exception=True)
def marca_create(request):
    form = MarcaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Marca creada exitosamente.')
        return redirect('marca_list')
    return render(request, 'ventas/marcas/formulario.html', {'form': form})


@login_required
@permission_required('ventas.change_marca', raise_exception=True)
def marca_update(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Marca editada exitosamente.')
        return redirect('marca_detail', pk=marca.pk)
    return render(request, 'ventas/marcas/formulario.html', {'form': form})


@login_required
@permission_required('ventas.delete_marca', raise_exception=True)
def marca_delete(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        messages.success(request, 'Marca eliminada exitosamente.')
        return redirect('marca_list')
    return render(request, 'ventas/marcas/marca_confirm_delete.html', {'marca': marca})
