from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render
from ..forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro completado exitosamente.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'ventas/auth/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Sesión iniciada.')
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'ventas/auth/login.html', {'form': form})


@require_POST
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesión cerrada.')
    return redirect('home')
