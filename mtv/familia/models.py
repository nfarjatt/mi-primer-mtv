from django.db import models
from concurrent.futures.process import _MAX_WINDOWS_WORKERS

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(maxlength=100)
    apellido = models.CharField(maxlength=100)
    email =  models.CharField(maxlength=100)
    fecha_nacimiento = models.DateField()
    