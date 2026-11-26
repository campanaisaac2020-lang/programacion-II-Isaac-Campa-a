from django.urls import path
from ..views.accesorio_views import accesorio_list, accesorio_detail, accesorio_create, accesorio_update, accesorio_delete

urlpatterns = [
    path('accesorios/', accesorio_list, name='accesorio_list'),
    path('accesorios/<int:pk>/', accesorio_detail, name='accesorio_detail'),
    path('accesorios/crear/', accesorio_create, name='accesorio_create'),
    path('accesorios/<int:pk>/editar/', accesorio_update, name='accesorio_update'),
    path('accesorios/<int:pk>/eliminar/', accesorio_delete, name='accesorio_delete'),
]
