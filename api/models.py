from django.db import models

# Create your models here.
class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=None)
    is_active = models.BooleanField(default=True)
    
class students(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    num_ficha = models.PositiveIntegerField(max_length=7, default=True)
    formacion = models.BooleanField(default=True)
    fecha_ingreso = models.DateField()
    is_active = models.BooleanField(default=True)