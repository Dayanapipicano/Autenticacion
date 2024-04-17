from django.db import models


# RELACION DE UNO A UNO ENTRE MODELOS
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    
class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.IntegerField()
    autores = models.OneToOneField(Autor, on_delete=models.CASCADE)
    
