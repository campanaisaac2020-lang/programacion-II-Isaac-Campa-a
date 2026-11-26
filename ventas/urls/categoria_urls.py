from django.urls import path
from ..views.categoria_views import *
urlpatterns=[
 path('categorias/', categoria_list, name='categoria_list'),
 path('categorias/<int:pk>/', categoria_detail, name='categoria_detail'),
 path('categorias/crear/', categoria_create, name='categoria_create'),
 path('categorias/<int:pk>/editar/', categoria_update, name='categoria_update'),
 path('categorias/<int:pk>/eliminar/', categoria_delete, name='categoria_delete'),
]
