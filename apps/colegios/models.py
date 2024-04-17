from django.db import models
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField('Estudiante')
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)


