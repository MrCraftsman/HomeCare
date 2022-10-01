from django.db import models
from .usuario import Usuario


class Familiar(models.Model):
    id_familiar= models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=35)
    apellidos = models.CharField('Apellidos', max_length=35)
    telefono  = models.CharField('Telefono', max_length=35)
    genero = models.CharField('Genero', max_length=35)
    direccion = models.CharField('Direccion', max_length=35)
    correo = models.EmailField('Correo', max_length=35)
    id_Usuario= models.ForeignKey(Usuario,related_name='familiar',on_delete=models.CASCADE)
