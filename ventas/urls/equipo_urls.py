from django.urls import path
from ..views.equipo_views import *
urlpatterns=[
 path('equipos/',equipo_list,name='equipo_list'),
 path('equipos/crear/',equipo_create,name='create_equipo'),
 path('equipos/<int:pk>/',equipo_detail,name='equipo_detail'),
 path('equipos/<int:pk>/editar/',equipo_update,name='update_equipo'),
 path('equipos/<int:pk>/eliminar/',equipo_delete,name='delete_equipo'),
]
