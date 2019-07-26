from django.db import models

# Create your models here.


editable = (
        ('1', 'Activo'),
        ('0', 'Inactivo'),
    )

class Municipio(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=editable)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=200)
    municipios = models.ManyToManyField(Municipio, blank=True)


    def __str__(self):
        return self.nombre