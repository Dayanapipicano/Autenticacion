from django.db import models

class ModelA(models.Model):
    nombre = models.CharField(max_length=100)
    
class ModelB(models.Model):
    nombre = models.CharField(max_length=100)
    modelo_a= models.OneToOneField(ModelA,on_delete=models.CASCADE)

    
