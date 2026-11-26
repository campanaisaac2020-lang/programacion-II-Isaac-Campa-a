from django.shortcuts import render


def rutas(request):
    rutas_data = [
        {'nombre': 'Ruta 1', 'origen': 'Norte', 'destino': 'Sur', 'tarifa': 0.35},
        {'nombre': 'Ruta 2', 'origen': 'Norte', 'destino': 'Sur', 'tarifa': 0.35},
        {'nombre': 'Ruta 3', 'origen': 'Norte', 'destino': 'Sur', 'tarifa': 0.35},
        {'nombre': 'Ruta 4', 'origen': 'Norte', 'destino': 'Sur', 'tarifa': 0.35},
        {'nombre': 'Ruta 5', 'origen': 'Norte', 'destino': 'Sur', 'tarifa': 0.35},
        {'nombre': 'Ruta Creada', 'origen': 'Oeste', 'destino': 'Este', 'tarifa': 5.00},
    ]
    return render(request, 'ventas/rutas.html', {'rutas': rutas_data})
