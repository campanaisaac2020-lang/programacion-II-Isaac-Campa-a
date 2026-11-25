from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from ..forms import CategoriaForm
from ..models import Categoria

def categoria_list(request):
    return render(request, 'ventas/categorias/categoria_list.html', {'categorias': Categoria.objects.all()})
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'ventas/categorias/categoria_detail.html', {'categoria': categoria})
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/formulario.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría editada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/formulario.html', {'form': form})
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(request, 'ventas/categorias/categoria_confirm_delete.html', {'categoria': categoria})
