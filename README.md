# Venta de equipos móviles
Proyecto Django sencillo para administrar equipos de teléfonos y sus categorías. No requiere crear una cuenta para consultar o modificar el catálogo.

## Modelos y relaciones

- `Categoria`: nombre y descripción de la categoría.
- `EquipoMovil`: marca escrita como texto, modelo, categoría, año, almacenamiento, precio, fecha de lanzamiento, descripción y disponibilidad (`Disponible` o `No disponible`).
- Cada equipo pertenece a una categoría. Desde el detalle de una categoría se puede ver sus equipos.

## Levantar el proyecto desde cero

```powershell
cd django/venta-celulares
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py iniciar_demo
python manage.py runserver
```

Después abre `http://127.0.0.1:8000/`. No se necesita iniciar sesión para usar la aplicación.

## Datos de prueba

El comando `python manage.py iniciar_demo` crea cinco categorías y cinco equipos de ejemplo. Se puede marcar cada teléfono como disponible o no disponible desde el formulario de creación o edición.

La aplicación incluye listados, detalles, creación, edición y eliminación de equipos y categorías.
