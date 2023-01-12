from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=50)

class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    precio = models.FloatField()

class Clases(models.Model):
    nombre = models.CharField(max_length=30)
    duracion = models.CharField(max_length=15)
    maestro = models.CharField(max_length=30)

