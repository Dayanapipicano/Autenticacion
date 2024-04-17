from django.db import models

#RELACION UNO A MUCHOS ENTRE MODELOS

class Fundador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    
class Casa(models.Model):
    nombre = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fundadorCasa = models.ForeignKey(Fundador, on_delete=models.CASCADE)
    
