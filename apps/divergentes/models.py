from django.db import models

#RELACION DE MUCHOS A MUCHOS ENTRE MODELOS 

class Faccion(models.Model):
    nombre = models.CharField(max_length=100)
    Miembros = models.ManyToManyField('Miembro')
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    facciones = models.ManyToManyField(Faccion)
    
    
    
