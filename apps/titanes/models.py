from django.db import models

class TitanUno(models.Model):
    nombre = models.CharField(max_length=100)
    
class TitanDos(models.Model):
    nombre = models.CharField(max_length=100)
    titan_uno = models.ManyToManyField(TitanUno)
    


