from django.db import models


#MODELO JUGADOR 
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)