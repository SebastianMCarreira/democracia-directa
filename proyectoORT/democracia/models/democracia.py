from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=128)

    def serialize(self):
        return {
            'id': self.pk,
            'nombre': self.nombre
        }

class Distrito(models.Model):
    nombre = models.CharField(max_length=128)

    def serialize(self):
        return {
            'id': self.pk,
            'nombre': self.nombre
        }