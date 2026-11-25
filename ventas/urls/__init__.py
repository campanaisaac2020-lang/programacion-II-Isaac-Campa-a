from django.urls import include, path

urlpatterns = [
    path('', include('ventas.urls.home_urls')),
    path('', include('ventas.urls.categoria_urls')),
    path('', include('ventas.urls.equipo_urls')),
]
