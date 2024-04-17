from django.db import models

class ModeloUno(models.Model):
    nombre = models.CharField(max_length=100)
    
class ModeloDos(models.Model):
    nombre = models.CharField(max_length=100)
    modelo_uno = models.ForeignKey(ModeloUno, on_delete=models.CASCADE)
    
