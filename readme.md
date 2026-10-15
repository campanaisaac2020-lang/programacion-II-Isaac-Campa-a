# Programación II

Repositorio de la materia **Programación II**, donde se organizan los proyectos, prácticas y subproyectos desarrollados durante el curso con **Python**, **Django** y **Odoo**.

---

## Tecnologías del curso

### 🐍 Python
Lenguaje de programación de alto nivel, interpretado y de propósito general. Se caracteriza por una sintaxis clara y legible que facilita el aprendizaje. Es la base de todo el curso, ya que tanto Django como Odoo están construidos sobre él.

**Usos principales:** automatización, análisis de datos, desarrollo web, inteligencia artificial y aplicaciones de escritorio.

🔗 [python.org](https://www.python.org/)

### 🌐 Django
Framework web de Python de código abierto que sigue el patrón **MTV** (Modelo – Plantilla – Vista). Permite crear sitios y aplicaciones web de forma rápida y segura, e incluye de serie un ORM para bases de datos, sistema de autenticación y un panel de administración.

**Usos principales:** aplicaciones web, APIs REST, sistemas de gestión y portales.

🔗 [djangoproject.com](https://www.djangoproject.com/)

### 🏢 Odoo
Plataforma **ERP** (planificación de recursos empresariales) de código abierto escrita en Python. Está formada por módulos integrados como ventas, inventario, contabilidad, compras y recursos humanos, y permite desarrollar módulos personalizados para adaptarla a las necesidades de cada empresa.

**Usos principales:** gestión empresarial, desarrollo de módulos a medida y automatización de procesos de negocio.

🔗 [odoo.com](https://www.odoo.com/)

---

## Estructura del repositorio

```
programacion-ii/
├── .gitignore
├── README.md
├── python/            # Ejercicios y proyectos en Python puro
│   ├── fundamentos/
│   └── proyectos/
├── django/            # Proyectos web con Django
│   └── nombre_proyecto/
└── odoo/              # Módulos personalizados de Odoo
    └── nombre_modulo/
```

---

## Requisitos

- Python 3.10 o superior
- Git
- pip y venv
- PostgreSQL (necesario para Odoo)

---

## Cómo empezar

Clonar el repositorio:

```bash
git clone git@github.com:USUARIO/programacion-ii.git
cd programacion-ii
```

Crear y activar un entorno virtual dentro del proyecto en el que se va a trabajar:

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

Instalar dependencias (si el proyecto tiene `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## Autor

**Isaac Campaña**
📧 campanaisaac2020@gmail.com