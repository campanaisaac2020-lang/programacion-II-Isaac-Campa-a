from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='EquipoMovil',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('anio', models.PositiveSmallIntegerField(
                    validators=[MinValueValidator(1980)],
                )),
                ('almacenamiento_gb', models.PositiveSmallIntegerField(
                    validators=[MinValueValidator(1)],
                    verbose_name='Almacenamiento (GB)',
                )),
                ('precio', models.DecimalField(
                    decimal_places=2,
                    max_digits=10,
                    validators=[MinValueValidator(0.01)],
                )),
                ('stock', models.PositiveIntegerField(
                    default=0,
                    verbose_name='Unidades disponibles',
                )),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Equipo móvil',
                'verbose_name_plural': 'Equipos móviles',
                'ordering': ['marca', 'modelo'],
            },
        ),
    ]
