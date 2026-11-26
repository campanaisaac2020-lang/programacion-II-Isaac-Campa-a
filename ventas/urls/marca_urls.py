from django.urls import path
from ..views.marca_views import marca_detail, marca_list

urlpatterns = [
    path('marcas/', marca_list, name='marca_list'),
    path('marcas/<int:pk>/', marca_detail, name='marca_detail'),
]
