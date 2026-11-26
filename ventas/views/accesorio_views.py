from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import AccesorioForm
from ..models import Accesorio


def accesorio_list(request):
    return render(request, 'ventas/accesorios/accesorio_list.html', {'accesorios': Accesorio.objects.all()})


def accesorio_detail(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)
    return render(request, 'ventas/accesorios/accesorio_detail.html', {'accesorio': accesorio})


@login_required
@permission_required('ventas.add_accesorio', raise_exception=True)
def accesorio_create(request):
    form = AccesorioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Accesorio creado exitosamente.')
        return redirect('accesorio_list')
    return render(request, 'ventas/accesorios/formulario.html', {'form': form})


@login_required
@permission_required('ventas.change_accesorio', raise_exception=True)
def accesorio_update(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)
    form = AccesorioForm(request.POST or None, instance=accesorio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Accesorio editado exitosamente.')
        return redirect('accesorio_detail', pk=accesorio.pk)
    return render(request, 'ventas/accesorios/formulario.html', {'form': form})


@login_required
@permission_required('ventas.delete_accesorio', raise_exception=True)
def accesorio_delete(request, pk):
    accesorio = get_object_or_404(Accesorio, pk=pk)
    if request.method == 'POST':
        accesorio.delete()
        messages.success(request, 'Accesorio eliminado exitosamente.')
        return redirect('accesorio_list')
    return render(request, 'ventas/accesorios/accesorio_confirm_delete.html', {'accesorio': accesorio})
