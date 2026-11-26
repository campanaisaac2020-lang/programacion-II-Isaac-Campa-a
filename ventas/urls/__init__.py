from django.urls import include, path

urlpatterns = [
    path('', include('ventas.urls.home_urls')),
    path('', include('ventas.urls.categoria_urls')),
    path('', include('ventas.urls.equipo_urls')),
    path('', include('ventas.urls.marca_urls')),
    path('', include('ventas.urls.accesorio_urls')),
    path('', include('ventas.urls.auth_urls')),
]
