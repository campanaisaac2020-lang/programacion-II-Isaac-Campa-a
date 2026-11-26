from django.urls import path
from ..views.accesorio_views import accesorio_detail, accesorio_list

urlpatterns = [
    path('accesorios/', accesorio_list, name='accesorio_list'),
    path('accesorios/<int:pk>/', accesorio_detail, name='accesorio_detail'),
]
