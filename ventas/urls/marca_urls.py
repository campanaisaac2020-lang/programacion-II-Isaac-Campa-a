from django.urls import path
from ..views.marca_views import (
    marca_create,
    marca_delete,
    marca_detail,
    marca_list,
    marca_update,
)

urlpatterns = [
    path('marcas/', marca_list, name='marca_list'),
    path('marcas/crear/', marca_create, name='marca_create'),
    path('marcas/<int:pk>/', marca_detail, name='marca_detail'),
    path('marcas/<int:pk>/editar/', marca_update, name='marca_update'),
    path('marcas/<int:pk>/eliminar/', marca_delete, name='marca_delete'),
]
