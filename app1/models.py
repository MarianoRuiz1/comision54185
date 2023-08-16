from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    numero_comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(default='correo@example.com')
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title