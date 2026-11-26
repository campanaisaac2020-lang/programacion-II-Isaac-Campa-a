# Venta de celulares

Aplicación web desarrollada con Django para administrar celulares, categorías, marcas y accesorios.

## Relaciones

- Categoría — Equipo móvil: ForeignKey, una categoría contiene varios equipos.
- Marca — Equipo móvil: ForeignKey, una marca fabrica varios equipos.
- Equipo móvil — Accesorio: ManyToMany.
- Marca incluye descripción y estado de disponibilidad para venta.
- Los registros tienen `creado_por` para aplicar propiedad.

## Levantar el proyecto

```bash
cd venta-celulares
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py iniciar_demo
python manage.py runserver
```

Abrir http://127.0.0.1:8000/.

## Datos de prueba

`python manage.py iniciar_demo` crea 5 categorías, 5 marcas, 5 accesorios y 5 equipos.

| Usuario | Contraseña | Grupo |
|---|---|---|
| admin | Admin123! | Superusuario |
| administrador | Admin123! | administradores |
| consultor | Consultor123! | consultores |
