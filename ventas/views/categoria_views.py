from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import CategoriaForm
from ..models import Categoria

def categoria_list(request):
    return render(request, 'ventas/categorias/categoria_list.html', {'categorias': Categoria.objects.all()})
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'ventas/categorias/categoria_detail.html', {'categoria': categoria})
@login_required
@permission_required('ventas.add_categoria', raise_exception=True)
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        categoria = form.save(commit=False)
        categoria.creado_por = request.user
        categoria.save()
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/formulario.html', {'form': form})

@login_required
@permission_required('ventas.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if (
        not request.user.groups.filter(name='administradores').exists()
        and categoria.creado_por_id != request.user.pk
    ):
        raise PermissionDenied
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría editada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/formulario.html', {'form': form})
@login_required
@permission_required('ventas.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if (
        not request.user.groups.filter(name='administradores').exists()
        and categoria.creado_por_id != request.user.pk
    ):
        raise PermissionDenied
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/categoria_confirm_delete.html', {'categoria': categoria})
