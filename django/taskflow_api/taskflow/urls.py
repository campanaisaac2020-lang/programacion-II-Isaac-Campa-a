# taskflow/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),   # ← monta las rutas de tasks en la raíz "/"
]