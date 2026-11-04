from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Telefonos(models.Model):
    Tipo_de_telefono = models.CharField(max_length=100)
    Marca_Telefono = models.TextField(blank=True)
    Gamma_Telefono = models.TextField(blank=True)
    Valor_Telefono = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Aprendices = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Marca_Telefono} {self.Tipo_de_telefono}" 

class Maestro(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Aprendis(models.Model):
    maestro = models.ForeignKey(
        Maestro,
        on_delete=models.CASCADE,
        related_name ='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField('Mision', related_name='aprendis')


class Perfil(models.Model):
    telefonos = models.OneToOneField(Telefonos, on_delete=models.CASCADE)
    aprendis = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfiles/')

class Mision(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_created=True)



class Trabajadores(models.Model):
    nombre= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    titulo= models.CharField(max_length=100)
    objetivo = models.CharField(max_length=300)

    trabajadores = models.ManyToManyField(
        Trabajadores,
        through='Participacion')

class Arreglos(models.Model):
    trabajadores = models.ForeignKey(
    Trabajadores,  
    on_delete=models.CASCADE)
    actividad = models.ForeignKey(
        Mision, on_delete= models.CASCADE)
    rol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Trabajadores.nombre} en {self.actividad.titulo}"

    



    