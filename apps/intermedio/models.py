from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Estudiante, through="Inscripcion")
    
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    
    





