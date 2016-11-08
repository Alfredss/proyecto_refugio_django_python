from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Creamos nuestro modelo Mascota (debe de estar en singular)

class Mascota(models.Model):
	folio = models.CharField(max_length = 10, primary_key = True)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()