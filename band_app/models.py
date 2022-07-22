from django.db import models

# Create your models here.

class Fan(models.Model):
    nombre = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Banda(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    pais = models.CharField(max_length=45)
    fans = models.ManyToManyField(Fan, related_name="bandas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




