from django.db import models


class Insumos(models.Model):
    insumo = models.CharField(max_length=40)
    unidad = models.CharField(max_length=40)
    precio =models.IntegerField()
    fecha = models.DateField()
    proveedor = models.CharField(max_length=40)
    familia = models.CharField(max_length=40)

class Tareas(models.Model):
    codigo = models.CharField(max_length=40)
    rubro = models.CharField(max_length=40)
    tarea = models.CharField(max_length=40)
    unidad = models.CharField(max_length=40)
    costo = models.IntegerField()
    fecha = models.DateField()
    especificacion = models.CharField(max_length=40)


class Rubros(models.Model):
    codigo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    
class Familias(models.Model):
    codigo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)

